"""Generated from Smithy shape ``com.amazonaws.quicksight#StepAliasMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.step_id


class StepAliasMapping(TypedDict):
    step_id: "aws_sdk_quicksight.types.step_id.StepId"
    """<p>The unique identifier of the step.</p>"""
    step_alias: "str"
    """<p>The alias for the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepAliasMapping) -> dict:
    out: dict = {}
    out["StepId"] = value["step_id"]
    out["StepAlias"] = value["step_alias"]
    return out


def deserialize_json(data: dict) -> StepAliasMapping:
    out: StepAliasMapping = {}  # type: ignore[typeddict-item]
    if "StepId" in data:
        out["step_id"] = data["StepId"]
    else:
        raise DeserializationError("StepAliasMapping.step_id required")
    if "StepAlias" in data:
        out["step_alias"] = data["StepAlias"]
    else:
        raise DeserializationError("StepAliasMapping.step_alias required")
    return out
