"""Generated from Smithy shape ``com.amazonaws.datazone#Member``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError


class _Member_userIdentifier(TypedDict, closed=True):
    userIdentifier: "str"


class _Member_groupIdentifier(TypedDict, closed=True):
    groupIdentifier: "str"


Member: TypeAlias = _Member_userIdentifier | _Member_groupIdentifier


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    if "userIdentifier" in value:
        return {"userIdentifier": value["userIdentifier"]}
    elif "groupIdentifier" in value:
        return {"groupIdentifier": value["groupIdentifier"]}
    else:
        raise SerializationError("Member: no variant present")


def deserialize_json(data: dict) -> Member:
    if "userIdentifier" in data:
        return {"userIdentifier": data["userIdentifier"]}
    elif "groupIdentifier" in data:
        return {"groupIdentifier": data["groupIdentifier"]}
    else:
        raise DeserializationError("Member: no recognized variant key")
