"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.orchestration_name_string


class BlueprintDetails(TypedDict, closed=True):
    blueprint_name: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The name of the blueprint.</p>"""
    run_id: NotRequired["capo_glue.types.id_string.IdString"]
    """<p>The run ID for this blueprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintDetails) -> dict:
    out: dict = {}
    if "blueprint_name" in value:
        out["BlueprintName"] = value["blueprint_name"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BlueprintDetails:
    out: BlueprintDetails = {}  # type: ignore[typeddict-item]
    if "BlueprintName" in data:
        out["blueprint_name"] = data["BlueprintName"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    return out
