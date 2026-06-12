"""Generated from Smithy shape ``com.amazonaws.glue#GetTriggerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.trigger


class GetTriggerResponse(TypedDict):
    trigger: NotRequired["aws_sdk_glue.types.trigger.Trigger"]
    """<p>The requested trigger definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTriggerResponse) -> dict:
    out: dict = {}
    if "trigger" in value:
        import aws_sdk_glue.types.trigger

        out["Trigger"] = aws_sdk_glue.types.trigger.serialize_aws_json_1_1(
            value["trigger"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTriggerResponse:
    out: GetTriggerResponse = {}  # type: ignore[typeddict-item]
    if "Trigger" in data:
        import aws_sdk_glue.types.trigger

        out["trigger"] = aws_sdk_glue.types.trigger.deserialize_aws_json_1_1(
            data["Trigger"]
        )
    return out
