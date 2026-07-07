"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteAvailabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.domain_name
    import aws_sdk_workmail.types.organization_id


class DeleteAvailabilityConfigurationRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be deleted.</p>"""
    domain_name: "aws_sdk_workmail.types.domain_name.DomainName"
    """<p>The domain for which the <code>AvailabilityConfiguration</code> will be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAvailabilityConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAvailabilityConfigurationRequest:
    out: DeleteAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteAvailabilityConfigurationRequest.organization_id required"
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "DeleteAvailabilityConfigurationRequest.domain_name required"
        )
    return out
