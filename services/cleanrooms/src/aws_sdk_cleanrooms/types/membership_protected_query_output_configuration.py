"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipProtectedQueryOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_query_s3_output_configuration


class _MembershipProtectedQueryOutputConfiguration_s3(TypedDict):
    s3: "aws_sdk_cleanrooms.types.protected_query_s3_output_configuration.ProtectedQueryS3OutputConfiguration"


MembershipProtectedQueryOutputConfiguration: TypeAlias = (
    _MembershipProtectedQueryOutputConfiguration_s3
)


# --- restJson1 ser/de ---
def serialize_json(value: MembershipProtectedQueryOutputConfiguration) -> dict:
    if "s3" in value:
        import aws_sdk_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": aws_sdk_cleanrooms.types.protected_query_s3_output_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError(
            "MembershipProtectedQueryOutputConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MembershipProtectedQueryOutputConfiguration:
    if "s3" in data:
        import aws_sdk_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": aws_sdk_cleanrooms.types.protected_query_s3_output_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        raise DeserializationError(
            "MembershipProtectedQueryOutputConfiguration: no recognized variant key"
        )
