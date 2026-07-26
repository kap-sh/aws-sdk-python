"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_distribute_output_configuration
    import capo_cleanrooms.types.protected_query_member_output_configuration
    import capo_cleanrooms.types.protected_query_s3_output_configuration


class _ProtectedQueryOutputConfiguration_s3(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_query_s3_output_configuration.ProtectedQueryS3OutputConfiguration"


class _ProtectedQueryOutputConfiguration_member(TypedDict, closed=True):
    member: "capo_cleanrooms.types.protected_query_member_output_configuration.ProtectedQueryMemberOutputConfiguration"


class _ProtectedQueryOutputConfiguration_distribute(TypedDict, closed=True):
    distribute: "capo_cleanrooms.types.protected_query_distribute_output_configuration.ProtectedQueryDistributeOutputConfiguration"


ProtectedQueryOutputConfiguration: TypeAlias = (
    _ProtectedQueryOutputConfiguration_s3
    | _ProtectedQueryOutputConfiguration_member
    | _ProtectedQueryOutputConfiguration_distribute
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryOutputConfiguration) -> dict:
    if "s3" in value:
        import capo_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "member" in value:
        import capo_cleanrooms.types.protected_query_member_output_configuration

        return {
            "member": capo_cleanrooms.types.protected_query_member_output_configuration.serialize_json(
                value["member"]
            )
        }
    elif "distribute" in value:
        import capo_cleanrooms.types.protected_query_distribute_output_configuration

        return {
            "distribute": capo_cleanrooms.types.protected_query_distribute_output_configuration.serialize_json(
                value["distribute"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedQueryOutputConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedQueryOutputConfiguration:
    if "s3" in data:
        import capo_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif "member" in data:
        import capo_cleanrooms.types.protected_query_member_output_configuration

        return {
            "member": capo_cleanrooms.types.protected_query_member_output_configuration.deserialize_json(
                data["member"]
            )
        }
    elif "distribute" in data:
        import capo_cleanrooms.types.protected_query_distribute_output_configuration

        return {
            "distribute": capo_cleanrooms.types.protected_query_distribute_output_configuration.deserialize_json(
                data["distribute"]
            )
        }
    else:
        raise DeserializationError(
            "ProtectedQueryOutputConfiguration: no recognized variant key"
        )
