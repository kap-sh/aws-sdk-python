"""Generated from Smithy shape ``com.amazonaws.route53domains#ContactDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.address_line
    import aws_sdk_route_53_domains.types.city
    import aws_sdk_route_53_domains.types.contact_name
    import aws_sdk_route_53_domains.types.contact_number
    import aws_sdk_route_53_domains.types.contact_type
    import aws_sdk_route_53_domains.types.country_code
    import aws_sdk_route_53_domains.types.email
    import aws_sdk_route_53_domains.types.extra_param_list
    import aws_sdk_route_53_domains.types.state
    import aws_sdk_route_53_domains.types.zip_code


class ContactDetail(TypedDict, closed=True):
    first_name: NotRequired["aws_sdk_route_53_domains.types.contact_name.ContactName"]
    """<p>First name of contact.</p>"""
    last_name: NotRequired["aws_sdk_route_53_domains.types.contact_name.ContactName"]
    """<p>Last name of contact.</p>"""
    contact_type: NotRequired["aws_sdk_route_53_domains.types.contact_type.ContactType"]
    r"""<p>Indicates whether the contact is a person, company, association, or public organization. Note the following:</p> <ul> <li> <p>If you specify a value other than <code>PERSON</code>, you must also specify a value for <code>OrganizationName</code>.</p> </li> <li> <p>For some TLDs, the privacy protection available depends on the value that you specify for <code>Contact Type</code>. For the privacy protection settings for your TLD, see <a href=\"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html\">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i> </p> </li> <li> <p>For .es domains, the value of <code>ContactType</code> must be <code>PERSON</code> for all three contacts.</p> </li> </ul>"""
    organization_name: NotRequired[
        "aws_sdk_route_53_domains.types.contact_name.ContactName"
    ]
    """<p>Name of the organization for contact types other than <code>PERSON</code>.</p>"""
    address_line1: NotRequired[
        "aws_sdk_route_53_domains.types.address_line.AddressLine"
    ]
    """<p>First line of the contact's address.</p>"""
    address_line2: NotRequired[
        "aws_sdk_route_53_domains.types.address_line.AddressLine"
    ]
    """<p>Second line of contact's address, if any.</p>"""
    city: NotRequired["aws_sdk_route_53_domains.types.city.City"]
    """<p>The city of the contact's address.</p>"""
    state: NotRequired["aws_sdk_route_53_domains.types.state.State"]
    """<p>The state or province of the contact's city.</p>"""
    country_code: NotRequired["aws_sdk_route_53_domains.types.country_code.CountryCode"]
    """<p>Code for the country of the contact's address.</p>"""
    zip_code: NotRequired["aws_sdk_route_53_domains.types.zip_code.ZipCode"]
    """<p>The zip or postal code of the contact's address.</p>"""
    phone_number: NotRequired[
        "aws_sdk_route_53_domains.types.contact_number.ContactNumber"
    ]
    r"""<p>The phone number of the contact.</p> <p>Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as <code>\"+1.1234567890\"</code>.</p>"""
    email: NotRequired["aws_sdk_route_53_domains.types.email.Email"]
    """<p>Email address of the contact.</p>"""
    fax: NotRequired["aws_sdk_route_53_domains.types.contact_number.ContactNumber"]
    r"""<p>Fax number of the contact.</p> <p>Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as <code>\"+1.1234567890\"</code>.</p>"""
    extra_params: NotRequired[
        "aws_sdk_route_53_domains.types.extra_param_list.ExtraParamList"
    ]
    """<p>A list of name-value pairs for parameters required by certain top-level domains.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactDetail) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "contact_type" in value:
        import aws_sdk_route_53_domains.types.contact_type

        out["ContactType"] = (
            aws_sdk_route_53_domains.types.contact_type.serialize_aws_json_1_1(
                value["contact_type"]
            )
        )
    if "organization_name" in value:
        out["OrganizationName"] = value["organization_name"]
    if "address_line1" in value:
        out["AddressLine1"] = value["address_line1"]
    if "address_line2" in value:
        out["AddressLine2"] = value["address_line2"]
    if "city" in value:
        out["City"] = value["city"]
    if "state" in value:
        out["State"] = value["state"]
    if "country_code" in value:
        import aws_sdk_route_53_domains.types.country_code

        out["CountryCode"] = (
            aws_sdk_route_53_domains.types.country_code.serialize_aws_json_1_1(
                value["country_code"]
            )
        )
    if "zip_code" in value:
        out["ZipCode"] = value["zip_code"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "email" in value:
        out["Email"] = value["email"]
    if "fax" in value:
        out["Fax"] = value["fax"]
    if "extra_params" in value:
        import aws_sdk_route_53_domains.types.extra_param_list

        out["ExtraParams"] = (
            aws_sdk_route_53_domains.types.extra_param_list.serialize_aws_json_1_1(
                value["extra_params"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContactDetail:
    out: ContactDetail = {}  # type: ignore[typeddict-item]
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "ContactType" in data:
        import aws_sdk_route_53_domains.types.contact_type

        out["contact_type"] = (
            aws_sdk_route_53_domains.types.contact_type.deserialize_aws_json_1_1(
                data["ContactType"]
            )
        )
    if "OrganizationName" in data:
        out["organization_name"] = data["OrganizationName"]
    if "AddressLine1" in data:
        out["address_line1"] = data["AddressLine1"]
    if "AddressLine2" in data:
        out["address_line2"] = data["AddressLine2"]
    if "City" in data:
        out["city"] = data["City"]
    if "State" in data:
        out["state"] = data["State"]
    if "CountryCode" in data:
        import aws_sdk_route_53_domains.types.country_code

        out["country_code"] = (
            aws_sdk_route_53_domains.types.country_code.deserialize_aws_json_1_1(
                data["CountryCode"]
            )
        )
    if "ZipCode" in data:
        out["zip_code"] = data["ZipCode"]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "Fax" in data:
        out["fax"] = data["Fax"]
    if "ExtraParams" in data:
        import aws_sdk_route_53_domains.types.extra_param_list

        out["extra_params"] = (
            aws_sdk_route_53_domains.types.extra_param_list.deserialize_aws_json_1_1(
                data["ExtraParams"]
            )
        )
    return out
