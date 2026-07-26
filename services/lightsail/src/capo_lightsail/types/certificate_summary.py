"""Generated from Smithy shape ``com.amazonaws.lightsail#CertificateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.certificate
    import capo_lightsail.types.certificate_name
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.tag_list


class CertificateSummary(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    certificate_name: NotRequired[
        "capo_lightsail.types.certificate_name.CertificateName"
    ]
    """<p>The name of the certificate.</p>"""
    domain_name: NotRequired["capo_lightsail.types.domain_name.DomainName"]
    """<p>The domain name of the certificate.</p>"""
    certificate_detail: NotRequired["capo_lightsail.types.certificate.Certificate"]
    """<p>An object that describes a certificate in detail.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    r"""<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateSummary) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "certificate_detail" in value:
        import capo_lightsail.types.certificate

        out["certificateDetail"] = (
            capo_lightsail.types.certificate.serialize_aws_json_1_1(
                value["certificate_detail"]
            )
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateSummary:
    out: CertificateSummary = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "certificateDetail" in data:
        import capo_lightsail.types.certificate

        out["certificate_detail"] = (
            capo_lightsail.types.certificate.deserialize_aws_json_1_1(
                data["certificateDetail"]
            )
        )
    if "tags" in data:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
