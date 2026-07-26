"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StepOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.data_type


class StepOutput(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""
    data_type: NotRequired["capo_migrationhuborchestrator.types.data_type.DataType"]
    """<p>The data type of the step output.</p>"""
    required: NotRequired["bool"]
    """<p>Determine if an output is required from a step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "data_type" in value:
        out["dataType"] = value["data_type"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> StepOutput:
    out: StepOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "dataType" in data:
        out["data_type"] = data["dataType"]
    if "required" in data:
        out["required"] = data["required"]
    return out
