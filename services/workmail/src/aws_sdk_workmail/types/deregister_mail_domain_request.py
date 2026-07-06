"""Generated from Smithy shape ``com.amazonaws.workmail#DeregisterMailDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.work_mail_domain_name


class DeregisterMailDomainRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the domain will be deregistered.</p>"""
    domain_name: "aws_sdk_workmail.types.work_mail_domain_name.WorkMailDomainName"
    """<p>The domain to deregister in WorkMail and SES.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterMailDomainRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterMailDomainRequest:
    out: DeregisterMailDomainRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeregisterMailDomainRequest.organization_id required"
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("DeregisterMailDomainRequest.domain_name required")
    return out
