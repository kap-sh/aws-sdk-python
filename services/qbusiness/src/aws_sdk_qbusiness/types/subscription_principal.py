"""Generated from Smithy shape ``com.amazonaws.qbusiness#SubscriptionPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.group_identifier
    import aws_sdk_qbusiness.types.user_identifier


class _SubscriptionPrincipal_user(TypedDict, closed=True):
    user: "aws_sdk_qbusiness.types.user_identifier.UserIdentifier"


class _SubscriptionPrincipal_group(TypedDict, closed=True):
    group: "aws_sdk_qbusiness.types.group_identifier.GroupIdentifier"


SubscriptionPrincipal: TypeAlias = (
    _SubscriptionPrincipal_user | _SubscriptionPrincipal_group
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionPrincipal) -> dict:
    if "user" in value:
        return {"user": value["user"]}
    elif "group" in value:
        return {"group": value["group"]}
    else:
        raise SerializationError("SubscriptionPrincipal: no variant present")


def deserialize_json(data: dict) -> SubscriptionPrincipal:
    if "user" in data:
        return {"user": data["user"]}
    elif "group" in data:
        return {"group": data["group"]}
    else:
        raise DeserializationError("SubscriptionPrincipal: no recognized variant key")
