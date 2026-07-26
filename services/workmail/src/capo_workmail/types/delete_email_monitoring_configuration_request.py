"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteEmailMonitoringConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.organization_id


class DeleteEmailMonitoringConfigurationRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The ID of the organization from which the email monitoring configuration is deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEmailMonitoringConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEmailMonitoringConfigurationRequest:
    out: DeleteEmailMonitoringConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteEmailMonitoringConfigurationRequest.organization_id required"
        )
    return out
