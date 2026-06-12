"""Generated from Smithy shape ``com.amazonaws.glue#UpdateTriggerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.trigger_update


class UpdateTriggerRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the trigger to update.</p>"""
    trigger_update: "aws_sdk_glue.types.trigger_update.TriggerUpdate"
    """<p>The new values with which to update the trigger.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTriggerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.trigger_update

    out["TriggerUpdate"] = aws_sdk_glue.types.trigger_update.serialize_aws_json_1_1(
        value["trigger_update"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTriggerRequest:
    out: UpdateTriggerRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateTriggerRequest.name required")
    if "TriggerUpdate" in data:
        import aws_sdk_glue.types.trigger_update

        out["trigger_update"] = (
            aws_sdk_glue.types.trigger_update.deserialize_aws_json_1_1(
                data["TriggerUpdate"]
            )
        )
    else:
        raise DeserializationError("UpdateTriggerRequest.trigger_update required")
    return out
