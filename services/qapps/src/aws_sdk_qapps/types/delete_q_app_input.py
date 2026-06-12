"""Generated from Smithy shape ``com.amazonaws.qapps#DeleteQAppInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class DeleteQAppInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQAppInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    return out


def deserialize_json(data: dict) -> DeleteQAppInput:
    out: DeleteQAppInput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("DeleteQAppInput.app_id required")
    return out
