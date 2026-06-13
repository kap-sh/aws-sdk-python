"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration
    import aws_sdk_cleanrooms.types.protected_query_member_output_configuration
    import aws_sdk_cleanrooms.types.protected_query_s3_output_configuration


class _ProtectedQueryOutputConfiguration_s3(TypedDict):
    s3: "aws_sdk_cleanrooms.types.protected_query_s3_output_configuration.ProtectedQueryS3OutputConfiguration"


class _ProtectedQueryOutputConfiguration_member(TypedDict):
    member: "aws_sdk_cleanrooms.types.protected_query_member_output_configuration.ProtectedQueryMemberOutputConfiguration"


class _ProtectedQueryOutputConfiguration_distribute(TypedDict):
    distribute: "aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration.ProtectedQueryDistributeOutputConfiguration"


ProtectedQueryOutputConfiguration: TypeAlias = (
    _ProtectedQueryOutputConfiguration_s3
    | _ProtectedQueryOutputConfiguration_member
    | _ProtectedQueryOutputConfiguration_distribute
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryOutputConfiguration) -> dict:
    if "s3" in value:
        import aws_sdk_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": aws_sdk_cleanrooms.types.protected_query_s3_output_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "member" in value:
        import aws_sdk_cleanrooms.types.protected_query_member_output_configuration

        return {
            "member": aws_sdk_cleanrooms.types.protected_query_member_output_configuration.serialize_json(
                value["member"]
            )
        }
    elif "distribute" in value:
        import aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration

        return {
            "distribute": aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration.serialize_json(
                value["distribute"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedQueryOutputConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedQueryOutputConfiguration:
    if "s3" in data:
        import aws_sdk_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": aws_sdk_cleanrooms.types.protected_query_s3_output_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif "member" in data:
        import aws_sdk_cleanrooms.types.protected_query_member_output_configuration

        return {
            "member": aws_sdk_cleanrooms.types.protected_query_member_output_configuration.deserialize_json(
                data["member"]
            )
        }
    elif "distribute" in data:
        import aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration

        return {
            "distribute": aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration.deserialize_json(
                data["distribute"]
            )
        }
    else:
        raise DeserializationError(
            "ProtectedQueryOutputConfiguration: no recognized variant key"
        )
