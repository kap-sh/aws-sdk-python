"""Generated from Smithy shape ``com.amazonaws.appflow#SlackSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.object


class SlackSourceProperties(TypedDict, closed=True):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Slack flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> SlackSourceProperties:
    out: SlackSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("SlackSourceProperties.object required")
    return out
