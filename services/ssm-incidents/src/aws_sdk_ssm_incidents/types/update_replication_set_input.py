"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateReplicationSetInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.client_token
    import aws_sdk_ssm_incidents.types.update_action_list


class UpdateReplicationSetInput(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the replication set you're updating.</p>"""
    actions: "aws_sdk_ssm_incidents.types.update_action_list.UpdateActionList"
    """<p>An action to add or delete a Region.</p>"""
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReplicationSetInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_ssm_incidents.types.update_action_list

    out["actions"] = aws_sdk_ssm_incidents.types.update_action_list.serialize_json(
        value["actions"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateReplicationSetInput:
    out: UpdateReplicationSetInput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateReplicationSetInput.arn required")
    if "actions" in data:
        import aws_sdk_ssm_incidents.types.update_action_list

        out["actions"] = (
            aws_sdk_ssm_incidents.types.update_action_list.deserialize_json(
                data["actions"]
            )
        )
    else:
        raise DeserializationError("UpdateReplicationSetInput.actions required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
