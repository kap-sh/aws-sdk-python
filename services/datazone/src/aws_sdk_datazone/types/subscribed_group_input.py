"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedGroupInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.group_profile_id


class SubscribedGroupInput(TypedDict):
    identifier: NotRequired["aws_sdk_datazone.types.group_profile_id.GroupProfileId"]
    """<p>The ID of the subscribed group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedGroupInput) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> SubscribedGroupInput:
    out: SubscribedGroupInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    return out
