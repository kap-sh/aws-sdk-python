"""Generated from Smithy shape ``com.amazonaws.personalizeevents#User``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.string_type
    import aws_sdk_personalize_events.types.synthesized_json_user_properties


class User(TypedDict):
    user_id: "aws_sdk_personalize_events.types.string_type.StringType"
    """<p>The ID associated with the user.</p>"""
    properties: NotRequired[
        "aws_sdk_personalize_events.types.synthesized_json_user_properties.SynthesizedJsonUserProperties"
    ]
    r"""<p>A string map of user-specific metadata. Each element in the map consists of a key-value pair. For example, <code>{\"numberOfVideosWatched\": \"45\"}</code>.</p> <p>The keys use camel case names that match the fields in the schema for the Users dataset. In the previous example, the <code>numberOfVideosWatched</code> matches the 'NUMBER_OF_VIDEOS_WATCHED' field defined in the Users schema. For categorical string data, to include multiple categories for a single user, separate each category with a pipe separator (<code>|</code>). For example, <code>\\"Member|Frequent shopper\\"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "properties" in value:
        out["properties"] = value["properties"]
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("User.user_id required")
    if "properties" in data:
        out["properties"] = data["properties"]
    return out
