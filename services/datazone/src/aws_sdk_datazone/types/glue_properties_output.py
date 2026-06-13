"""Generated from Smithy shape ``com.amazonaws.datazone#GluePropertiesOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.connection_status


class GluePropertiesOutput(TypedDict):
    status: NotRequired["aws_sdk_datazone.types.connection_status.ConnectionStatus"]
    """<p>The status of a connection.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message generated if the action is not completed successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GluePropertiesOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_datazone.types.connection_status

        out["status"] = aws_sdk_datazone.types.connection_status.serialize_json(
            value["status"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> GluePropertiesOutput:
    out: GluePropertiesOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_datazone.types.connection_status

        out["status"] = aws_sdk_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
