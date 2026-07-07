"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UserIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.identity_id


class UserIdentity(TypedDict, closed=True):
    id: "aws_sdk_iotsitewise.types.identity_id.IdentityId"
    """<p>The IAM Identity Center ID of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentity) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> UserIdentity:
    out: UserIdentity = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UserIdentity.id required")
    return out
