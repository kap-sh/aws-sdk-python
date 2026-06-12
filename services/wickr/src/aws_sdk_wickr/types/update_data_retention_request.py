"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateDataRetentionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.data_retention_action_type
    import aws_sdk_wickr.types.network_id


class UpdateDataRetentionRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the data retention bot.</p>"""
    action_type: (
        "aws_sdk_wickr.types.data_retention_action_type.DataRetentionActionType"
    )
    """<p>The action to perform. Valid values are 'ENABLE' (to enable the data retention service), 'DISABLE' (to disable the service), or 'PUBKEY_MSG_ACK' (to acknowledge the public key message).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataRetentionRequest) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.data_retention_action_type

    out["actionType"] = aws_sdk_wickr.types.data_retention_action_type.serialize_json(
        value["action_type"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataRetentionRequest:
    out: UpdateDataRetentionRequest = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        import aws_sdk_wickr.types.data_retention_action_type

        out["action_type"] = (
            aws_sdk_wickr.types.data_retention_action_type.deserialize_json(
                data["actionType"]
            )
        )
    else:
        raise DeserializationError("UpdateDataRetentionRequest.action_type required")
    return out
