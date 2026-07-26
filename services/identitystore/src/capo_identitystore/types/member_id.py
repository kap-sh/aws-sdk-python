"""Generated from Smithy shape ``com.amazonaws.identitystore#MemberId``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_identitystore.types.resource_id


class _MemberId_UserId(TypedDict, closed=True):
    UserId: "capo_identitystore.types.resource_id.ResourceId"


MemberId: TypeAlias = _MemberId_UserId


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberId) -> dict:
    if "UserId" in value:
        return {"UserId": value["UserId"]}
    else:
        raise SerializationError("MemberId: no variant present")


def deserialize_aws_json_1_1(data: dict) -> MemberId:
    if "UserId" in data:
        return {"UserId": data["UserId"]}
    else:
        raise DeserializationError("MemberId: no recognized variant key")
