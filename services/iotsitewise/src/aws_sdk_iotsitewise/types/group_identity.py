"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GroupIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.identity_id


class GroupIdentity(TypedDict):
    id: "aws_sdk_iotsitewise.types.identity_id.IdentityId"
    """<p>The IAM Identity Center ID of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupIdentity) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> GroupIdentity:
    out: GroupIdentity = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GroupIdentity.id required")
    return out
