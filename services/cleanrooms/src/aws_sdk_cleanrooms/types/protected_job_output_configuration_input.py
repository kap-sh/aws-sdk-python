"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobOutputConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_member_output_configuration_input


class _ProtectedJobOutputConfigurationInput_member(TypedDict, closed=True):
    member: "aws_sdk_cleanrooms.types.protected_job_member_output_configuration_input.ProtectedJobMemberOutputConfigurationInput"


ProtectedJobOutputConfigurationInput: TypeAlias = (
    _ProtectedJobOutputConfigurationInput_member
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobOutputConfigurationInput) -> dict:
    if "member" in value:
        import aws_sdk_cleanrooms.types.protected_job_member_output_configuration_input

        return {
            "member": aws_sdk_cleanrooms.types.protected_job_member_output_configuration_input.serialize_json(
                value["member"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedJobOutputConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedJobOutputConfigurationInput:
    if "member" in data:
        import aws_sdk_cleanrooms.types.protected_job_member_output_configuration_input

        return {
            "member": aws_sdk_cleanrooms.types.protected_job_member_output_configuration_input.deserialize_json(
                data["member"]
            )
        }
    else:
        raise DeserializationError(
            "ProtectedJobOutputConfigurationInput: no recognized variant key"
        )
