"""Generated from Smithy shape ``com.amazonaws.securityhub#Target``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class _Target_AccountId(TypedDict, closed=True):
    AccountId: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"


class _Target_OrganizationalUnitId(TypedDict, closed=True):
    OrganizationalUnitId: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"


class _Target_RootId(TypedDict, closed=True):
    RootId: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"


Target: TypeAlias = _Target_AccountId | _Target_OrganizationalUnitId | _Target_RootId


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> dict:
    if "AccountId" in value:
        return {"AccountId": value["AccountId"]}
    elif "OrganizationalUnitId" in value:
        return {"OrganizationalUnitId": value["OrganizationalUnitId"]}
    elif "RootId" in value:
        return {"RootId": value["RootId"]}
    else:
        raise SerializationError("Target: no variant present")


def deserialize_json(data: dict) -> Target:
    if "AccountId" in data:
        return {"AccountId": data["AccountId"]}
    elif "OrganizationalUnitId" in data:
        return {"OrganizationalUnitId": data["OrganizationalUnitId"]}
    elif "RootId" in data:
        return {"RootId": data["RootId"]}
    else:
        raise DeserializationError("Target: no recognized variant key")
