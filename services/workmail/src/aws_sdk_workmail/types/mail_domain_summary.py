"""Generated from Smithy shape ``com.amazonaws.workmail#MailDomainSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.boolean
    import aws_sdk_workmail.types.domain_name


class MailDomainSummary(TypedDict):
    domain_name: NotRequired["aws_sdk_workmail.types.domain_name.DomainName"]
    """<p>The domain name.</p>"""
    default_domain: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>Whether the domain is default or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MailDomainSummary) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    out["DefaultDomain"] = value.get("default_domain", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> MailDomainSummary:
    out: MailDomainSummary = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "DefaultDomain" in data:
        out["default_domain"] = data["DefaultDomain"]
    else:
        out["default_domain"] = False
    return out
