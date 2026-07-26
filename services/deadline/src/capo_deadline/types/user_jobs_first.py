"""Generated from Smithy shape ``com.amazonaws.deadline#UserJobsFirst``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.string


class UserJobsFirst(TypedDict, closed=True):
    user_identity_id: "capo_deadline.types.string.String"
    """<p>The user's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserJobsFirst) -> dict:
    out: dict = {}
    out["userIdentityId"] = value["user_identity_id"]
    return out


def deserialize_json(data: dict) -> UserJobsFirst:
    out: UserJobsFirst = {}  # type: ignore[typeddict-item]
    if "userIdentityId" in data:
        out["user_identity_id"] = data["userIdentityId"]
    else:
        raise DeserializationError("UserJobsFirst.user_identity_id required")
    return out
