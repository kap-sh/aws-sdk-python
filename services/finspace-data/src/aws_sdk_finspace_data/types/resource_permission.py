"""Generated from Smithy shape ``com.amazonaws.finspacedata#ResourcePermission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.string_value_length1to250


class ResourcePermission(TypedDict):
    permission: NotRequired[
        "aws_sdk_finspace_data.types.string_value_length1to250.StringValueLength1to250"
    ]
    """<p>Permission for a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePermission) -> dict:
    out: dict = {}
    if "permission" in value:
        out["permission"] = value["permission"]
    return out


def deserialize_json(data: dict) -> ResourcePermission:
    out: ResourcePermission = {}  # type: ignore[typeddict-item]
    if "permission" in data:
        out["permission"] = data["permission"]
    return out
