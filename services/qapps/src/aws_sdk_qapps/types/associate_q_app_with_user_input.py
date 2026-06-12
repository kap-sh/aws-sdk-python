"""Generated from Smithy shape ``com.amazonaws.qapps#AssociateQAppWithUserInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class AssociateQAppWithUserInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The ID of the Amazon Q App to associate with the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateQAppWithUserInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    return out


def deserialize_json(data: dict) -> AssociateQAppWithUserInput:
    out: AssociateQAppWithUserInput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("AssociateQAppWithUserInput.app_id required")
    return out
