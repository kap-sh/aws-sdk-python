"""Generated from Smithy shape ``com.amazonaws.ssmsap#StartApplicationRefreshOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.operation_id


class StartApplicationRefreshOutput(TypedDict, closed=True):
    operation_id: NotRequired["aws_sdk_ssm_sap.types.operation_id.OperationId"]
    """<p>The ID of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApplicationRefreshOutput) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_json(data: dict) -> StartApplicationRefreshOutput:
    out: StartApplicationRefreshOutput = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
