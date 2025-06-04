# Importing required functions 
from flask import Flask, request, render_template, redirect, url_for
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email_id = "jasonaprice99@gmail.com"
sender_email_id_password = "ethw wbwt yqsb bzkf"
receiver_email_id = ["jasonaprice99@gmail.com"]

model = ChatOpenAI(model_name="deepseek-chat", api_key="sk-ddbcaf44325949eeb97a0671895e33a6", base_url="https://api.deepseek.com")

# Flask constructor 
app = Flask(__name__)
simpleData = {}
detailData = {}

# Define a global variable to store form data
global_data = {}

def calculate_score(features):
    # Define the scoring dictionary
    scoringDict = {
        "Play room": 90,
        "Outdoor play equipment": 85,
        "Baby listening": 80,
        "Wifi": 80,
        "Swimming pool": 75,
        "Babysitting": 70,
        "Kids club/creche": 65,
        "Farm animals": 60,
        "Restaurant": 55,
        "Hot tubs": 50,
        "Bar": 45,
        "Spa": 40,
        "Electric vehicle charging": 25,
        "Golf": 20
    }
    return sum(scoringDict.get(feature, 0) for feature in features)

def classify_score(score):
    if score > 630:
        return "Green"
    elif 420 <= score <= 629:
        return "Yellow"
    else:
        return "Red"

def sendEmail(data):
	# Extract the data from the global variable
    form1_data = global_data.get('form1', {})
    accommodation_data = global_data.get('accommodation', {})
    vitals_data = global_data.get('vitals', {})
    age_groups_data = global_data.get('age_groups', {})
    features_data = global_data.get('features', {})
    print(features_data)
    score = calculate_score(features_data)
    classification = classify_score(score)
    
    print(score)

    detailedReport = f"""
    Away with the Kids: Company Overview and Services
    Away with the Kids is an independent UK-based travel website (launched 2008/09) devoted entirely to family-friendly holidays. It connects families with child-focused accommodations and destinations, offering curated listings of cottages, villas, farm stays, B&Bs, hotels, glamping sites and more that are 1 2 
suitable for children . The site features over 400 vetted, “meticulously evaluated” family-friendly 1 2 
properties worldwide . In addition to searchable listings, AWK provides editorial content and travel inspiration (blogs, destination guides, special collections of kids’ activities, etc.) tailored to parents. Industry observers note that AWK aims to simplify family travel: The Good Web Guide calls it “a genius site” supplying “everything required for the modern family,” with “baby, child and (perhaps most 3 
importantly of all) parent-friendly holidays” that avert most holiday stress .  
Ethos and Values 
Away with the Kids is built on a family-first philosophy. It was founded by a parent frustrated by unreliable reviews of child-suitable accommodation, so trust and accuracy are core values . 
1 2 
1 
AWK’s team itself “operates remotely, embodying a ‘family first’ ethos” . Every property on AWK is required to meet strict family standards: the platform “only represents holiday accommodation that meets our child-friendly standards,” meaning each listing must genuinely cater to kids . In 
1 2 
practice, this means the company highlights safety, comfort and convenience for children (for example by promoting fenced pools, gated play areas, and amenities like cots/highchairs), while also addressing parents’ needs. The overall goal is to give parents confidence – AWK strives to eliminate the usual 3 1 
hassles by pre-vetting child-friendly features and letting families plan with peace of mind .  Property Listing Requirements and Features 
AWK does not publish a detailed public checklist, but any listed property must be genuinely family oriented. Commonly expected features include: 
- Safety and childproofing. Pools (if present) should be fully fenced/gated and meet safety regulations. Living spaces often have stair-gates, corner protectors or other childproofing. Outdoor areas (gardens, balconies, farm fields) are secured so young children can play safely. 
- Family amenities. Listings typically include essentials like travel cots/cribs, highchairs, baby monitors and children’s cutlery. Many properties also offer toys, books, games, swings or small playgrounds to keep kids entertained. Kitchenettes (with kettles, microwaves etc.) and laundry facilities are often highlighted for family convenience. 
- Adequate space. Multiple bedrooms and bathrooms are common to accommodate family groups. Additional sleeping areas (sofas or daybeds) and ample floor space (e.g. room for a travel cot or playpen) are important. 
- Child-focused extras. Unique or “wow” features are a plus. For example, some properties emphasize 1

pets or farm animals to feed, on-site playrooms, kids’ TV or media rooms, or easy access to child oriented attractions (beach, park, farm visit, etc.). Many AWK listings note when they have dedicated children’s menu in the dining room, family-friendly gardens or seasonal kids’ entertainment. - General comfort. Features like simple kitchen facilities, laundry, and secure lock-up storage are valued by parents. Good communications (clear Wi-Fi access, detailed arrival instructions) and professional responsiveness (helpful owners/managers) also align with AWK’s standard of “meticulously 1 
evaluated, family-friendly accommodations” .  
In short, a property will only be listed if it truly lives up to AWK’s family-friendly ethos. Owners are expected to document all amenities and safety features in their listing. AWK’s review team checks 1 
each submission to ensure that these child-friendly standards are met .  
Owner Application and Listing Process 
Property owners or managers must apply and meet certain requirements to be featured on AWK. The main steps are:  
•  
Submit the “Get Listed” application. Interested owners complete the online Get-Listed form, 4 
providing their name, email, phone, property name, location, type and website . They confirm they’ve read AWK’s terms.  
•  
Approval and account setup. AWK reviews the submission. If the property meets their criteria, the owner is notified by email and given login credentials. The owner then accesses the AWK 4 
Owner Admin portal to create a full listing .  
•  
Create the listing. In the Owner Admin interface, the owner fills in all details about the property. This includes writing descriptions and specifying the location, and especially uploading photos of 5 
each unit . Owners categorize the property correctly (e.g. “child friendly cottages,” “glamping,” etc.). They enter the number and types of units/rooms available, plus any relevant policies (e.g. pet policy, cancellation terms). All listed amenities and child-friendly features should be entered here, since AWK will display these to parents.  
•  
Set availability and pricing. Owners add pricing for each unit (seasonal rates) and availability calendars. They can connect their own Property Management System (PMS) if it’s compatible, or 6 
manually enter iCal calendar links . This keeps AWK’s booking system in sync with the owner’s other channels.  
•  
Configure payments. Owners link a payment processor (Stripe or GoCardless) so guest payments flow directly to them. AWK provides tools within the admin to “Connect to Stripe” or 7 
“Connect to GoCardless,” which handle commissions and deposits .  
•  
Pay fees. Publishing the listing requires payment of AWK’s listing fee. Per the contract, owners 8 
“agree to pay… the listing rate as advertised for the publishing of any listing” . (In practice this fee is typically taken as a credit against future commission invoices.)  
•  
Handle bookings and commissions. Once live, AWK will refer guests to book through the 
platform. Owners must collect payments from guests and then pay AWK its agreed commission on each booking. The contract stipulates that owners “agree to pay [AWK] a commission on each 9 
reservation,” calculated as a percentage of the booking total . Commissions are invoiced monthly or automatically deducted depending on the payment setup.  
5 8 
Throughout this process, owners must keep all information accurate and up to date . AWK provides detailed user guides and email support (info@awaywiththekids.co.uk) if owners have questions about any step.  
2
Sources: Official AWK and partner materials (company website, owner terms) and reputable travel 1 2 3 10 8 9 
industry articles . Each cited source provides insight into AWK’s services, values, and requirements. 
    """
    scoringList = """Play room,90
Outdoor play equipment,85
Baby listening,80
Wifi,80
Swimming Pool,75
Babysitting,70
Kids club/creche,65
Farm animals,60
Restaurant,55
Hot Tubs,50
Bar,45
Spa,40
Electric vehicle charging,25
Golf,20"""
    template1 = """
    Answer the question below.

Here is the detailed report of the company: {detailedReport}

Here is the all the data from the application for context: {context}

Question: {question}

Scoring List: {scoringList}
Features in the property: {features_data}
Score: {score}
Classification: {classification}

Write a professional email to the business owner about new application for someone to join their platform. The data provided in the converstaion history describes the property that has applied for the platform.
Write with using the context of the detailed report of the company and the data from the application.
This email will include in the body, a description of the property, the features in the property, and the score for the property, and further steps for the business owner to carry out like accepting/rejecting the application or further things the business owner wants details in.
The email body will follow the structure of the following:
- Receiving a new application for someone to join the platform.
- Classification of the property.
- Score of the property.
- Description and features of the property.
- Next steps for the business owner to take such as accepting or rejecting the application, for the property to then be listed on the site.

- This email is to be sent to the business owner of the platform.
- This email is send from the business AI assistant.

For formatting, use the following:
- Use **bold** for the important points in the email body but do not bold the subject.

Template:
"Subject: Enter the subject here"
"Body: Enter the body here"
"""
    template = """
Answer the question below.

Here is the detailed report of the company: {detailedReport}

Here is the all the data from the application for context: {context}

Question: {question}

Scoring List: {scoringList}
Features in the property: {features_data}
Score: {score}
Add a paragraph in the email body to say the score for the property and if it is highly rated.

Instructions:
- If the question is about the subject, return a concise and professional email subject.
- If the question is about the body, return a detailed and polite email body without a subject.
- For both cases, the email is to a business owner about new application for someone to join their platform. The data provided in the converstaion history describes the property that has applied for the platform.
- It should also outline the next steps for the business owner to take such as accepting or rejecting the application, for the property to then be listed on the site.
- This email is to be sent to the business owner of the platform.
- This email is send from the business AI assistant.
- The email should summarise all the information provided in the conversation history.
- This is a business email, so be professional and polite.
- In both cases, remove all formatting and special characters.


Template:
"Subject: [Enter the subject here]"
"Body: [Enter the body here]"
"""
    prompt = PromptTemplate.from_template(template1)
	
    chain = prompt | model
    context = f"{form1_data}{accommodation_data}{vitals_data}{age_groups_data}{features_data}"
    subjectQuery = "Could you write an email based on the context?"
    result = chain.invoke({"detailedReport": detailedReport, "context": context, "question": subjectQuery, "scoringList": scoringList, "features_data": features_data, "score": score, "classification": classification})
    result_content = result.content.strip()
    print(result_content)
    subject = ""
    body = ""
    if "Subject:" in result_content and "Body:" in result_content:
        subject_start = result_content.find("Subject:") + len("Subject:")
        body_start = result_content.find("Body:")
        subject = result_content[subject_start:body_start].strip()
        body = result_content[body_start + len("Body:"):].strip()
        # Remove any newlines and asterisks from subject to avoid HeaderWriteError and unwanted formatting
        subject = subject.replace('\n', ' ').replace('\r', ' ').strip()
        # Remove leading/trailing asterisks and spaces from subject
        while subject.startswith("*") or subject.startswith(" "):
            subject = subject[1:]
        while subject.endswith("*") or subject.endswith(" "):
            subject = subject[:-1]
        # Remove leading asterisks and newlines from body
        body = body.lstrip('* \n\r')

    print(subject)
    print(body)

    # Convert **bold** to <b>bold</b> for HTML emails
    import re
    def markdown_bold_to_html(text):
        # Convert ###**text** or ### **text** to <u><b>text</b></u>
        text = re.sub(r'###\s*\*\*(.*?)\*\*', r'<u><b>\1</b></u>', text)
        # Convert remaining **bold** to <b>bold</b>
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        # Convert double newlines to paragraphs
        paragraphs = [f"<p>{p.strip()}</p>" for p in text.split('\n\n') if p.strip()]
        html = "<br>".join(paragraphs)
        # Convert single newlines to <br> within paragraphs
        html = re.sub(r'(?<!<br>)\n', '<br>', html)
        return html

    html_body = markdown_bold_to_html(body)

    # Create a MIME message for HTML email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email_id
    msg["To"] = ", ".join(receiver_email_id)
    part = MIMEText(html_body, "html")
    msg.attach(part)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email_id, sender_email_id_password)
    # send the HTML email
    s.sendmail(sender_email_id, receiver_email_id, msg.as_string())
    s.quit()
    print("Email sent successfully!")

# Root endpoint 
@app.route('/', methods=['GET']) 
def index(): 
	## Display the HTML form template 
	return render_template('index.html') 

# `read-form` endpoint 
@app.route('/read-form', methods=['POST']) 
def read_form():
    global global_data
    data = request.form
    global_data['form1'] = data.to_dict()
    return redirect(url_for('accommodation'))

@app.route('/accommodation', methods=['GET', 'POST'])
def accommodation():
    global global_data
    if request.method == 'POST':
        global_data['age_groups'] = request.form.getlist('age_groups[]')
        global_data['accommodation'] = request.form.getlist('accommodation[]')
        return redirect(url_for('features'))
    return render_template('accommodation.html')

@app.route('/vitals', methods=['GET', 'POST'])
def vitals():
    global global_data
    if request.method == 'POST':
        global_data['vitals'] = request.form.getlist('vitals[]')
        return redirect(url_for('age_groups'))
    return render_template('vitals.html')

@app.route('/age_groups', methods=['GET', 'POST'])
def age_groups():
    global global_data
    if request.method == 'POST':
        global_data['age_groups'] = request.form.getlist('age_groups[]')
        return redirect(url_for('submit_further_details'))
    # Pass global_data to the template to avoid UndefinedError
    return render_template('review.html', global_data=global_data)

@app.route('/features', methods=['GET', 'POST'])
def features():
    global global_data
    if request.method == 'POST':
        global_data['vitals'] = request.form.getlist('vitals[]')
        global_data['features'] = request.form.getlist('features[]')
        return redirect(url_for('age_groups'))
    return render_template('features.html')

@app.route('/submit-further-details', methods=['GET'])
def submit_further_details():
    global global_data
    # Get the form data from furtherDetails.html
    data = request.form

    # Update the global variable with data from the second form
    global_data['form2'] = data.to_dict()
    sendEmail(global_data)
    print(global_data)

    # Return a success message or redirect to another page
    return render_template('final.html')
# Main Driver Function 
if __name__ == '__main__': 
	# Run the application on the local development server 
	app.run()