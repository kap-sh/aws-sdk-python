"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#UpdateAppInstanceUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.metadata
    import aws_sdk_chime_sdk_identity.types.user_name


class UpdateAppInstanceUserRequest(TypedDict, closed=True):
    app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    name: "aws_sdk_chime_sdk_identity.types.user_name.UserName"
    """<p>The name of the <code>AppInstanceUser</code>.</p>"""
    metadata: "aws_sdk_chime_sdk_identity.types.metadata.Metadata"
    """<p>The metadata of the <code>AppInstanceUser</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppInstanceUserRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> UpdateAppInstanceUserRequest:
    out: UpdateAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateAppInstanceUserRequest.name required")
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    else:
        raise DeserializationError("UpdateAppInstanceUserRequest.metadata required")
    return out
