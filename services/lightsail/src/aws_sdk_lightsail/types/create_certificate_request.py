"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_name
    import aws_sdk_lightsail.types.domain_name
    import aws_sdk_lightsail.types.subject_alternative_name_list
    import aws_sdk_lightsail.types.tag_list


class CreateCertificateRequest(TypedDict, closed=True):
    certificate_name: "aws_sdk_lightsail.types.certificate_name.CertificateName"
    """<p>The name for the certificate.</p>"""
    domain_name: "aws_sdk_lightsail.types.domain_name.DomainName"
    """<p>The domain name (<code>example.com</code>) for the certificate.</p>"""
    subject_alternative_names: NotRequired[
        "aws_sdk_lightsail.types.subject_alternative_name_list.SubjectAlternativeNameList"
    ]
    """<p>An array of strings that specify the alternate domains (<code>example2.com</code>) and subdomains (<code>blog.example.com</code>) for the certificate.</p> <p>You can specify a maximum of nine alternate domains (in addition to the primary domain name).</p> <p>Wildcard domain entries (<code>*.example.com</code>) are not supported.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the certificate during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCertificateRequest) -> dict:
    out: dict = {}
    out["certificateName"] = value["certificate_name"]
    out["domainName"] = value["domain_name"]
    if "subject_alternative_names" in value:
        import aws_sdk_lightsail.types.subject_alternative_name_list

        out["subjectAlternativeNames"] = (
            aws_sdk_lightsail.types.subject_alternative_name_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCertificateRequest:
    out: CreateCertificateRequest = {}  # type: ignore[typeddict-item]
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    else:
        raise DeserializationError("CreateCertificateRequest.certificate_name required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("CreateCertificateRequest.domain_name required")
    if "subjectAlternativeNames" in data:
        import aws_sdk_lightsail.types.subject_alternative_name_list

        out["subject_alternative_names"] = (
            aws_sdk_lightsail.types.subject_alternative_name_list.deserialize_aws_json_1_1(
                data["subjectAlternativeNames"]
            )
        )
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
