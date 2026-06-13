"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerUserProperties``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.user_identifier


class OwnerUserProperties(TypedDict):
    user_identifier: "aws_sdk_datazone.types.user_identifier.UserIdentifier"
    """<p>The ID of the owner user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerUserProperties) -> dict:
    out: dict = {}
    out["userIdentifier"] = value["user_identifier"]
    return out


def deserialize_json(data: dict) -> OwnerUserProperties:
    out: OwnerUserProperties = {}  # type: ignore[typeddict-item]
    if "userIdentifier" in data:
        out["user_identifier"] = data["userIdentifier"]
    else:
        raise DeserializationError("OwnerUserProperties.user_identifier required")
    return out
