"""Generated from Smithy shape ``com.amazonaws.qapps#ExportQAppSessionDataInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class ExportQAppSessionDataInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    session_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App data collection session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportQAppSessionDataInput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> ExportQAppSessionDataInput:
    out: ExportQAppSessionDataInput = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("ExportQAppSessionDataInput.session_id required")
    return out
