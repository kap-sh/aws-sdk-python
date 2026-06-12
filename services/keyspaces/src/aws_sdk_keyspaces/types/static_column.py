"""Generated from Smithy shape ``com.amazonaws.keyspaces#StaticColumn``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.generic_string


class StaticColumn(TypedDict):
    name: "aws_sdk_keyspaces.types.generic_string.GenericString"
    """<p>The name of the static column.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StaticColumn) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StaticColumn:
    out: StaticColumn = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StaticColumn.name required")
    return out
