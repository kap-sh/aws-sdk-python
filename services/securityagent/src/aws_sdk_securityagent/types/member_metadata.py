"""Generated from Smithy shape ``com.amazonaws.securityagent#MemberMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.user_metadata


class _MemberMetadata_user(TypedDict, closed=True):
    user: "aws_sdk_securityagent.types.user_metadata.UserMetadata"


MemberMetadata: TypeAlias = _MemberMetadata_user


# --- restJson1 ser/de ---
def serialize_json(value: MemberMetadata) -> dict:
    if "user" in value:
        import aws_sdk_securityagent.types.user_metadata

        return {
            "user": aws_sdk_securityagent.types.user_metadata.serialize_json(
                value["user"]
            )
        }
    else:
        raise SerializationError("MemberMetadata: no variant present")


def deserialize_json(data: dict) -> MemberMetadata:
    if "user" in data:
        import aws_sdk_securityagent.types.user_metadata

        return {
            "user": aws_sdk_securityagent.types.user_metadata.deserialize_json(
                data["user"]
            )
        }
    else:
        raise DeserializationError("MemberMetadata: no recognized variant key")
