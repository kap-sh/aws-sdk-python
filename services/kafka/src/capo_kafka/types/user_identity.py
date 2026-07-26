"""Generated from Smithy shape ``com.amazonaws.kafka#UserIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.user_identity_type


class UserIdentity(TypedDict, closed=True):
    type: NotRequired["capo_kafka.types.user_identity_type.UserIdentityType"]
    """<p>The identity type of the requester that calls the API operation.</p>"""
    principal_id: NotRequired["capo_kafka.types.__string.__string"]
    """<p>A unique identifier for the requester that calls the API operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentity) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_kafka.types.user_identity_type

        out["type"] = capo_kafka.types.user_identity_type.serialize_json(value["type"])
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    return out


def deserialize_json(data: dict) -> UserIdentity:
    out: UserIdentity = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_kafka.types.user_identity_type

        out["type"] = capo_kafka.types.user_identity_type.deserialize_json(data["type"])
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    return out
