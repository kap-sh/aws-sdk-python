"""Generated from Smithy shape ``com.amazonaws.glue#StartTriggerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class StartTriggerResponse(TypedDict):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the trigger that was started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTriggerResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTriggerResponse:
    out: StartTriggerResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
