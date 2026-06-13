"""Generated from Smithy shape ``com.amazonaws.ssmsap#StartApplicationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.operation_id


class StartApplicationOutput(TypedDict):
    operation_id: NotRequired["aws_sdk_ssm_sap.types.operation_id.OperationId"]
    """<p>The ID of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApplicationOutput) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_json(data: dict) -> StartApplicationOutput:
    out: StartApplicationOutput = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
