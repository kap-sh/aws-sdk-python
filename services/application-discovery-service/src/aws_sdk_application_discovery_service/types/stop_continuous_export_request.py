"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StopContinuousExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configurations_export_id


class StopContinuousExportRequest(TypedDict):
    export_id: "aws_sdk_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
    """<p>The unique ID assigned to this export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopContinuousExportRequest) -> dict:
    out: dict = {}
    out["exportId"] = value["export_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopContinuousExportRequest:
    out: StopContinuousExportRequest = {}  # type: ignore[typeddict-item]
    if "exportId" in data:
        out["export_id"] = data["exportId"]
    else:
        raise DeserializationError("StopContinuousExportRequest.export_id required")
    return out
