"""Generated from Smithy shape ``com.amazonaws.glue#UpdateTriggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.trigger


class UpdateTriggerResponse(TypedDict, closed=True):
    trigger: NotRequired["capo_glue.types.trigger.Trigger"]
    """<p>The resulting trigger definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTriggerResponse) -> dict:
    out: dict = {}
    if "trigger" in value:
        import capo_glue.types.trigger

        out["Trigger"] = capo_glue.types.trigger.serialize_aws_json_1_1(
            value["trigger"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTriggerResponse:
    out: UpdateTriggerResponse = {}  # type: ignore[typeddict-item]
    if "Trigger" in data:
        import capo_glue.types.trigger

        out["trigger"] = capo_glue.types.trigger.deserialize_aws_json_1_1(
            data["Trigger"]
        )
    return out
