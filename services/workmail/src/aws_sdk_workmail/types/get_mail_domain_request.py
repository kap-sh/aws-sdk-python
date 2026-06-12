"""Generated from Smithy shape ``com.amazonaws.workmail#GetMailDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.work_mail_domain_name


class GetMailDomainRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the domain is retrieved.</p>"""
    domain_name: "aws_sdk_workmail.types.work_mail_domain_name.WorkMailDomainName"
    """<p>The domain from which you want to retrieve details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMailDomainRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMailDomainRequest:
    out: GetMailDomainRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("GetMailDomainRequest.organization_id required")
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("GetMailDomainRequest.domain_name required")
    return out
