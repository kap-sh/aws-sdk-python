"""Generated from Smithy shape ``com.amazonaws.qconnect#CustomerProfileAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.custom_attributes
    import capo_qconnect.types.message_template_attribute_value


class CustomerProfileAttributes(TypedDict, closed=True):
    profile_id: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The unique identifier of a customer profile.</p>"""
    profile_arn: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The ARN of a customer profile.</p>"""
    first_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's first name.</p>"""
    middle_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's middle name.</p>"""
    last_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's last name.</p>"""
    account_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>A unique account number that you have given to the customer.</p>"""
    email_address: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's email address, which has not been specified as a personal or business address.</p>"""
    phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's phone number, which has not been specified as a mobile, home, or business number.</p>"""
    additional_information: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>Any additional information relevant to the customer's profile.</p>"""
    party_type: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's party type.</p>"""
    business_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The name of the customer's business.</p>"""
    birth_date: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's birth date.</p>"""
    gender: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's gender.</p>"""
    mobile_phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's mobile phone number.</p>"""
    home_phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's mobile phone number.</p>"""
    business_phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's business phone number.</p>"""
    business_email_address: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's business email address.</p>"""
    address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer address.</p>"""
    address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer address.</p>"""
    address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer address.</p>"""
    address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer address.</p>"""
    city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city in which a customer lives.</p>"""
    county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county in which a customer lives.</p>"""
    country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country in which a customer lives.</p>"""
    postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer address.</p>"""
    province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province in which a customer lives.</p>"""
    state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state in which a customer lives.</p>"""
    shipping_address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer’s shipping address.</p>"""
    shipping_address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer’s shipping address.</p>"""
    shipping_address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer’s shipping address.</p>"""
    shipping_address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer’s shipping address.</p>"""
    shipping_city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city of a customer’s shipping address.</p>"""
    shipping_county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county of a customer’s shipping address.</p>"""
    shipping_country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country of a customer’s shipping address.</p>"""
    shipping_postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer’s shipping address.</p>"""
    shipping_province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province of a customer’s shipping address.</p>"""
    shipping_state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state of a customer’s shipping address.</p>"""
    mailing_address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer’s mailing address.</p>"""
    mailing_address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer’s mailing address.</p>"""
    mailing_address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer’s mailing address.</p>"""
    mailing_address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer’s mailing address.</p>"""
    mailing_city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city of a customer’s mailing address.</p>"""
    mailing_county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county of a customer’s mailing address.</p>"""
    mailing_country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country of a customer’s mailing address.</p>"""
    mailing_postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer’s mailing address.</p>"""
    mailing_province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province of a customer’s mailing address.</p>"""
    mailing_state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state of a customer’s mailing address.</p>"""
    billing_address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer’s billing address.</p>"""
    billing_address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer’s billing address.</p>"""
    billing_address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer’s billing address.</p>"""
    billing_address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer’s billing address.</p>"""
    billing_city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city of a customer’s billing address.</p>"""
    billing_county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county of a customer’s billing address.</p>"""
    billing_country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country of a customer’s billing address.</p>"""
    billing_postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer’s billing address.</p>"""
    billing_province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province of a customer’s billing address.</p>"""
    billing_state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state of a customer’s billing address.</p>"""
    custom: NotRequired["capo_qconnect.types.custom_attributes.CustomAttributes"]
    """<p>The custom attributes in customer profile attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfileAttributes) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    if "profile_arn" in value:
        out["profileARN"] = value["profile_arn"]
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "middle_name" in value:
        out["middleName"] = value["middle_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "account_number" in value:
        out["accountNumber"] = value["account_number"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "phone_number" in value:
        out["phoneNumber"] = value["phone_number"]
    if "additional_information" in value:
        out["additionalInformation"] = value["additional_information"]
    if "party_type" in value:
        out["partyType"] = value["party_type"]
    if "business_name" in value:
        out["businessName"] = value["business_name"]
    if "birth_date" in value:
        out["birthDate"] = value["birth_date"]
    if "gender" in value:
        out["gender"] = value["gender"]
    if "mobile_phone_number" in value:
        out["mobilePhoneNumber"] = value["mobile_phone_number"]
    if "home_phone_number" in value:
        out["homePhoneNumber"] = value["home_phone_number"]
    if "business_phone_number" in value:
        out["businessPhoneNumber"] = value["business_phone_number"]
    if "business_email_address" in value:
        out["businessEmailAddress"] = value["business_email_address"]
    if "address1" in value:
        out["address1"] = value["address1"]
    if "address2" in value:
        out["address2"] = value["address2"]
    if "address3" in value:
        out["address3"] = value["address3"]
    if "address4" in value:
        out["address4"] = value["address4"]
    if "city" in value:
        out["city"] = value["city"]
    if "county" in value:
        out["county"] = value["county"]
    if "country" in value:
        out["country"] = value["country"]
    if "postal_code" in value:
        out["postalCode"] = value["postal_code"]
    if "province" in value:
        out["province"] = value["province"]
    if "state" in value:
        out["state"] = value["state"]
    if "shipping_address1" in value:
        out["shippingAddress1"] = value["shipping_address1"]
    if "shipping_address2" in value:
        out["shippingAddress2"] = value["shipping_address2"]
    if "shipping_address3" in value:
        out["shippingAddress3"] = value["shipping_address3"]
    if "shipping_address4" in value:
        out["shippingAddress4"] = value["shipping_address4"]
    if "shipping_city" in value:
        out["shippingCity"] = value["shipping_city"]
    if "shipping_county" in value:
        out["shippingCounty"] = value["shipping_county"]
    if "shipping_country" in value:
        out["shippingCountry"] = value["shipping_country"]
    if "shipping_postal_code" in value:
        out["shippingPostalCode"] = value["shipping_postal_code"]
    if "shipping_province" in value:
        out["shippingProvince"] = value["shipping_province"]
    if "shipping_state" in value:
        out["shippingState"] = value["shipping_state"]
    if "mailing_address1" in value:
        out["mailingAddress1"] = value["mailing_address1"]
    if "mailing_address2" in value:
        out["mailingAddress2"] = value["mailing_address2"]
    if "mailing_address3" in value:
        out["mailingAddress3"] = value["mailing_address3"]
    if "mailing_address4" in value:
        out["mailingAddress4"] = value["mailing_address4"]
    if "mailing_city" in value:
        out["mailingCity"] = value["mailing_city"]
    if "mailing_county" in value:
        out["mailingCounty"] = value["mailing_county"]
    if "mailing_country" in value:
        out["mailingCountry"] = value["mailing_country"]
    if "mailing_postal_code" in value:
        out["mailingPostalCode"] = value["mailing_postal_code"]
    if "mailing_province" in value:
        out["mailingProvince"] = value["mailing_province"]
    if "mailing_state" in value:
        out["mailingState"] = value["mailing_state"]
    if "billing_address1" in value:
        out["billingAddress1"] = value["billing_address1"]
    if "billing_address2" in value:
        out["billingAddress2"] = value["billing_address2"]
    if "billing_address3" in value:
        out["billingAddress3"] = value["billing_address3"]
    if "billing_address4" in value:
        out["billingAddress4"] = value["billing_address4"]
    if "billing_city" in value:
        out["billingCity"] = value["billing_city"]
    if "billing_county" in value:
        out["billingCounty"] = value["billing_county"]
    if "billing_country" in value:
        out["billingCountry"] = value["billing_country"]
    if "billing_postal_code" in value:
        out["billingPostalCode"] = value["billing_postal_code"]
    if "billing_province" in value:
        out["billingProvince"] = value["billing_province"]
    if "billing_state" in value:
        out["billingState"] = value["billing_state"]
    if "custom" in value:
        import capo_qconnect.types.custom_attributes

        out["custom"] = capo_qconnect.types.custom_attributes.serialize_json(
            value["custom"]
        )
    return out


def deserialize_json(data: dict) -> CustomerProfileAttributes:
    out: CustomerProfileAttributes = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    if "profileARN" in data:
        out["profile_arn"] = data["profileARN"]
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "middleName" in data:
        out["middle_name"] = data["middleName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    if "accountNumber" in data:
        out["account_number"] = data["accountNumber"]
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    if "phoneNumber" in data:
        out["phone_number"] = data["phoneNumber"]
    if "additionalInformation" in data:
        out["additional_information"] = data["additionalInformation"]
    if "partyType" in data:
        out["party_type"] = data["partyType"]
    if "businessName" in data:
        out["business_name"] = data["businessName"]
    if "birthDate" in data:
        out["birth_date"] = data["birthDate"]
    if "gender" in data:
        out["gender"] = data["gender"]
    if "mobilePhoneNumber" in data:
        out["mobile_phone_number"] = data["mobilePhoneNumber"]
    if "homePhoneNumber" in data:
        out["home_phone_number"] = data["homePhoneNumber"]
    if "businessPhoneNumber" in data:
        out["business_phone_number"] = data["businessPhoneNumber"]
    if "businessEmailAddress" in data:
        out["business_email_address"] = data["businessEmailAddress"]
    if "address1" in data:
        out["address1"] = data["address1"]
    if "address2" in data:
        out["address2"] = data["address2"]
    if "address3" in data:
        out["address3"] = data["address3"]
    if "address4" in data:
        out["address4"] = data["address4"]
    if "city" in data:
        out["city"] = data["city"]
    if "county" in data:
        out["county"] = data["county"]
    if "country" in data:
        out["country"] = data["country"]
    if "postalCode" in data:
        out["postal_code"] = data["postalCode"]
    if "province" in data:
        out["province"] = data["province"]
    if "state" in data:
        out["state"] = data["state"]
    if "shippingAddress1" in data:
        out["shipping_address1"] = data["shippingAddress1"]
    if "shippingAddress2" in data:
        out["shipping_address2"] = data["shippingAddress2"]
    if "shippingAddress3" in data:
        out["shipping_address3"] = data["shippingAddress3"]
    if "shippingAddress4" in data:
        out["shipping_address4"] = data["shippingAddress4"]
    if "shippingCity" in data:
        out["shipping_city"] = data["shippingCity"]
    if "shippingCounty" in data:
        out["shipping_county"] = data["shippingCounty"]
    if "shippingCountry" in data:
        out["shipping_country"] = data["shippingCountry"]
    if "shippingPostalCode" in data:
        out["shipping_postal_code"] = data["shippingPostalCode"]
    if "shippingProvince" in data:
        out["shipping_province"] = data["shippingProvince"]
    if "shippingState" in data:
        out["shipping_state"] = data["shippingState"]
    if "mailingAddress1" in data:
        out["mailing_address1"] = data["mailingAddress1"]
    if "mailingAddress2" in data:
        out["mailing_address2"] = data["mailingAddress2"]
    if "mailingAddress3" in data:
        out["mailing_address3"] = data["mailingAddress3"]
    if "mailingAddress4" in data:
        out["mailing_address4"] = data["mailingAddress4"]
    if "mailingCity" in data:
        out["mailing_city"] = data["mailingCity"]
    if "mailingCounty" in data:
        out["mailing_county"] = data["mailingCounty"]
    if "mailingCountry" in data:
        out["mailing_country"] = data["mailingCountry"]
    if "mailingPostalCode" in data:
        out["mailing_postal_code"] = data["mailingPostalCode"]
    if "mailingProvince" in data:
        out["mailing_province"] = data["mailingProvince"]
    if "mailingState" in data:
        out["mailing_state"] = data["mailingState"]
    if "billingAddress1" in data:
        out["billing_address1"] = data["billingAddress1"]
    if "billingAddress2" in data:
        out["billing_address2"] = data["billingAddress2"]
    if "billingAddress3" in data:
        out["billing_address3"] = data["billingAddress3"]
    if "billingAddress4" in data:
        out["billing_address4"] = data["billingAddress4"]
    if "billingCity" in data:
        out["billing_city"] = data["billingCity"]
    if "billingCounty" in data:
        out["billing_county"] = data["billingCounty"]
    if "billingCountry" in data:
        out["billing_country"] = data["billingCountry"]
    if "billingPostalCode" in data:
        out["billing_postal_code"] = data["billingPostalCode"]
    if "billingProvince" in data:
        out["billing_province"] = data["billingProvince"]
    if "billingState" in data:
        out["billing_state"] = data["billingState"]
    if "custom" in data:
        import capo_qconnect.types.custom_attributes

        out["custom"] = capo_qconnect.types.custom_attributes.deserialize_json(
            data["custom"]
        )
    return out
