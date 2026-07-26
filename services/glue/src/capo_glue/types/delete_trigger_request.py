"""Generated from Smithy shape ``com.amazonaws.glue#DeleteTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.name_string


class DeleteTriggerRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the trigger to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTriggerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTriggerRequest:
    out: DeleteTriggerRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteTriggerRequest.name required")
    return out
