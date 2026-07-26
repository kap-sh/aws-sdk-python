"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartExportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configurations_export_id


class StartExportTaskResponse(TypedDict, closed=True):
    export_id: NotRequired[
        "capo_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
    ]
    """<p>A unique identifier used to query the status of an export request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartExportTaskResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportId"] = value["export_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartExportTaskResponse:
    out: StartExportTaskResponse = {}  # type: ignore[typeddict-item]
    if "exportId" in data:
        out["export_id"] = data["exportId"]
    return out
