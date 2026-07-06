"""Generated from Smithy shape ``com.amazonaws.glue#GetBlueprintRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.orchestration_name_string


class GetBlueprintRunRequest(TypedDict, closed=True):
    blueprint_name: (
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    )
    """<p>The name of the blueprint.</p>"""
    run_id: "aws_sdk_glue.types.id_string.IdString"
    """<p>The run ID for the blueprint run you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintRunRequest) -> dict:
    out: dict = {}
    out["BlueprintName"] = value["blueprint_name"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintRunRequest:
    out: GetBlueprintRunRequest = {}  # type: ignore[typeddict-item]
    if "BlueprintName" in data:
        out["blueprint_name"] = data["BlueprintName"]
    else:
        raise DeserializationError("GetBlueprintRunRequest.blueprint_name required")
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("GetBlueprintRunRequest.run_id required")
    return out
