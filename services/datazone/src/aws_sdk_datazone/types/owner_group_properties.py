"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerGroupProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.group_identifier


class OwnerGroupProperties(TypedDict):
    group_identifier: "aws_sdk_datazone.types.group_identifier.GroupIdentifier"
    """<p>The ID of the domain unit owners group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerGroupProperties) -> dict:
    out: dict = {}
    out["groupIdentifier"] = value["group_identifier"]
    return out


def deserialize_json(data: dict) -> OwnerGroupProperties:
    out: OwnerGroupProperties = {}  # type: ignore[typeddict-item]
    if "groupIdentifier" in data:
        out["group_identifier"] = data["groupIdentifier"]
    else:
        raise DeserializationError("OwnerGroupProperties.group_identifier required")
    return out
