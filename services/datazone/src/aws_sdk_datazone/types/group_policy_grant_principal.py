"""Generated from Smithy shape ``com.amazonaws.datazone#GroupPolicyGrantPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.group_identifier


class _GroupPolicyGrantPrincipal_groupIdentifier(TypedDict, closed=True):
    groupIdentifier: "aws_sdk_datazone.types.group_identifier.GroupIdentifier"


GroupPolicyGrantPrincipal: TypeAlias = _GroupPolicyGrantPrincipal_groupIdentifier


# --- restJson1 ser/de ---
def serialize_json(value: GroupPolicyGrantPrincipal) -> dict:
    if "groupIdentifier" in value:
        return {"groupIdentifier": value["groupIdentifier"]}
    else:
        raise SerializationError("GroupPolicyGrantPrincipal: no variant present")


def deserialize_json(data: dict) -> GroupPolicyGrantPrincipal:
    if "groupIdentifier" in data:
        return {"groupIdentifier": data["groupIdentifier"]}
    else:
        raise DeserializationError(
            "GroupPolicyGrantPrincipal: no recognized variant key"
        )
