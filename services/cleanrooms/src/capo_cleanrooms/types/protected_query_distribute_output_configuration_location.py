"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryDistributeOutputConfigurationLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_member_output_configuration
    import capo_cleanrooms.types.protected_query_s3_output_configuration


class _ProtectedQueryDistributeOutputConfigurationLocation_s3(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_query_s3_output_configuration.ProtectedQueryS3OutputConfiguration"


class _ProtectedQueryDistributeOutputConfigurationLocation_member(
    TypedDict, closed=True
):
    member: "capo_cleanrooms.types.protected_query_member_output_configuration.ProtectedQueryMemberOutputConfiguration"


ProtectedQueryDistributeOutputConfigurationLocation: TypeAlias = (
    _ProtectedQueryDistributeOutputConfigurationLocation_s3
    | _ProtectedQueryDistributeOutputConfigurationLocation_member
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryDistributeOutputConfigurationLocation) -> dict:
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
    else:
        raise SerializationError(
            "ProtectedQueryDistributeOutputConfigurationLocation: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedQueryDistributeOutputConfigurationLocation:
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
    else:
        raise DeserializationError(
            "ProtectedQueryDistributeOutputConfigurationLocation: no recognized variant key"
        )
