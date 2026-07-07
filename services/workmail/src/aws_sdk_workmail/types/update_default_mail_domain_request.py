"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateDefaultMailDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.work_mail_domain_name


class UpdateDefaultMailDomainRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which to list domains.</p>"""
    domain_name: "aws_sdk_workmail.types.work_mail_domain_name.WorkMailDomainName"
    """<p>The domain name that will become the default domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDefaultMailDomainRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDefaultMailDomainRequest:
    out: UpdateDefaultMailDomainRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "UpdateDefaultMailDomainRequest.organization_id required"
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "UpdateDefaultMailDomainRequest.domain_name required"
        )
    return out
