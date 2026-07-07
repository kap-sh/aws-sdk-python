"""Generated from Smithy shape ``com.amazonaws.interconnect#RemoteAccountIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_interconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.remote_owner_account


class _RemoteAccountIdentifier_identifier(TypedDict, closed=True):
    identifier: "aws_sdk_interconnect.types.remote_owner_account.RemoteOwnerAccount"


RemoteAccountIdentifier: TypeAlias = _RemoteAccountIdentifier_identifier


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RemoteAccountIdentifier) -> dict:
    if "identifier" in value:
        return {"identifier": value["identifier"]}
    else:
        raise SerializationError("RemoteAccountIdentifier: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RemoteAccountIdentifier:
    if "identifier" in data:
        return {"identifier": data["identifier"]}
    else:
        raise DeserializationError("RemoteAccountIdentifier: no recognized variant key")
