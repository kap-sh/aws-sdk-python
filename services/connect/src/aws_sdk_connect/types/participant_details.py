"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.display_name


class ParticipantDetails(TypedDict):
    display_name: "aws_sdk_connect.types.display_name.DisplayName"
    """<p>Display name of the participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantDetails) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> ParticipantDetails:
    out: ParticipantDetails = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("ParticipantDetails.display_name required")
    return out
