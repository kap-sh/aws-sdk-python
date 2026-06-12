"""Generated from Smithy shape ``com.amazonaws.acmpca#ASN1Subject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.asn1_printable_string64
    import aws_sdk_acm_pca.types.country_code_string
    import aws_sdk_acm_pca.types.custom_attribute_list
    import aws_sdk_acm_pca.types.string3
    import aws_sdk_acm_pca.types.string5
    import aws_sdk_acm_pca.types.string16
    import aws_sdk_acm_pca.types.string40
    import aws_sdk_acm_pca.types.string64
    import aws_sdk_acm_pca.types.string128


class ASN1Subject(TypedDict):
    country: NotRequired["aws_sdk_acm_pca.types.country_code_string.CountryCodeString"]
    """<p>Two-digit code that specifies the country in which the certificate subject located.</p>"""
    organization: NotRequired["aws_sdk_acm_pca.types.string64.String64"]
    """<p>Legal name of the organization with which the certificate subject is affiliated. </p>"""
    organizational_unit: NotRequired["aws_sdk_acm_pca.types.string64.String64"]
    """<p>A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.</p>"""
    distinguished_name_qualifier: NotRequired[
        "aws_sdk_acm_pca.types.asn1_printable_string64.ASN1PrintableString64"
    ]
    """<p>Disambiguating information for the certificate subject.</p>"""
    state: NotRequired["aws_sdk_acm_pca.types.string128.String128"]
    """<p>State in which the subject of the certificate is located.</p>"""
    common_name: NotRequired["aws_sdk_acm_pca.types.string64.String64"]
    """<p>For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit. </p> <p>Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.</p>"""
    serial_number: NotRequired[
        "aws_sdk_acm_pca.types.asn1_printable_string64.ASN1PrintableString64"
    ]
    """<p>The certificate serial number.</p>"""
    locality: NotRequired["aws_sdk_acm_pca.types.string128.String128"]
    """<p>The locality (such as a city or town) in which the certificate subject is located.</p>"""
    title: NotRequired["aws_sdk_acm_pca.types.string64.String64"]
    """<p>A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.</p>"""
    surname: NotRequired["aws_sdk_acm_pca.types.string40.String40"]
    """<p>Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.</p>"""
    given_name: NotRequired["aws_sdk_acm_pca.types.string16.String16"]
    """<p>First name.</p>"""
    initials: NotRequired["aws_sdk_acm_pca.types.string5.String5"]
    """<p>Concatenation that typically contains the first letter of the <b>GivenName</b>, the first letter of the middle name if one exists, and the first letter of the <b>Surname</b>.</p>"""
    pseudonym: NotRequired["aws_sdk_acm_pca.types.string128.String128"]
    """<p>Typically a shortened version of a longer <b>GivenName</b>. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.</p>"""
    generation_qualifier: NotRequired["aws_sdk_acm_pca.types.string3.String3"]
    """<p>Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.</p>"""
    custom_attributes: NotRequired[
        "aws_sdk_acm_pca.types.custom_attribute_list.CustomAttributeList"
    ]
    """<p/> <p>Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST’s definition of <a href=\"https://csrc.nist.gov/glossary/term/Object_Identifier\">Object Identifier (OID)</a>.</p> <note> <p>Custom attributes cannot be used in combination with standard attributes.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ASN1Subject) -> dict:
    out: dict = {}
    if "country" in value:
        out["Country"] = value["country"]
    if "organization" in value:
        out["Organization"] = value["organization"]
    if "organizational_unit" in value:
        out["OrganizationalUnit"] = value["organizational_unit"]
    if "distinguished_name_qualifier" in value:
        out["DistinguishedNameQualifier"] = value["distinguished_name_qualifier"]
    if "state" in value:
        out["State"] = value["state"]
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "locality" in value:
        out["Locality"] = value["locality"]
    if "title" in value:
        out["Title"] = value["title"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "initials" in value:
        out["Initials"] = value["initials"]
    if "pseudonym" in value:
        out["Pseudonym"] = value["pseudonym"]
    if "generation_qualifier" in value:
        out["GenerationQualifier"] = value["generation_qualifier"]
    if "custom_attributes" in value:
        import aws_sdk_acm_pca.types.custom_attribute_list

        out["CustomAttributes"] = (
            aws_sdk_acm_pca.types.custom_attribute_list.serialize_aws_json_1_1(
                value["custom_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ASN1Subject:
    out: ASN1Subject = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        out["country"] = data["Country"]
    if "Organization" in data:
        out["organization"] = data["Organization"]
    if "OrganizationalUnit" in data:
        out["organizational_unit"] = data["OrganizationalUnit"]
    if "DistinguishedNameQualifier" in data:
        out["distinguished_name_qualifier"] = data["DistinguishedNameQualifier"]
    if "State" in data:
        out["state"] = data["State"]
    if "CommonName" in data:
        out["common_name"] = data["CommonName"]
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "Locality" in data:
        out["locality"] = data["Locality"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Surname" in data:
        out["surname"] = data["Surname"]
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    if "Initials" in data:
        out["initials"] = data["Initials"]
    if "Pseudonym" in data:
        out["pseudonym"] = data["Pseudonym"]
    if "GenerationQualifier" in data:
        out["generation_qualifier"] = data["GenerationQualifier"]
    if "CustomAttributes" in data:
        import aws_sdk_acm_pca.types.custom_attribute_list

        out["custom_attributes"] = (
            aws_sdk_acm_pca.types.custom_attribute_list.deserialize_aws_json_1_1(
                data["CustomAttributes"]
            )
        )
    return out
