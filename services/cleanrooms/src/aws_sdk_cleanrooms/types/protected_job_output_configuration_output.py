"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobOutputConfigurationOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_member_output_configuration_output
    import aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_output


class _ProtectedJobOutputConfigurationOutput_s3(TypedDict):
    s3: "aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_output.ProtectedJobS3OutputConfigurationOutput"


class _ProtectedJobOutputConfigurationOutput_member(TypedDict):
    member: "aws_sdk_cleanrooms.types.protected_job_member_output_configuration_output.ProtectedJobMemberOutputConfigurationOutput"


ProtectedJobOutputConfigurationOutput: TypeAlias = (
    _ProtectedJobOutputConfigurationOutput_s3
    | _ProtectedJobOutputConfigurationOutput_member
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobOutputConfigurationOutput) -> dict:
    if "s3" in value:
        import aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_output

        return {
            "s3": aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_output.serialize_json(
                value["s3"]
            )
        }
    elif "member" in value:
        import aws_sdk_cleanrooms.types.protected_job_member_output_configuration_output

        return {
            "member": aws_sdk_cleanrooms.types.protected_job_member_output_configuration_output.serialize_json(
                value["member"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedJobOutputConfigurationOutput: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedJobOutputConfigurationOutput:
    if "s3" in data:
        import aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_output

        return {
            "s3": aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_output.deserialize_json(
                data["s3"]
            )
        }
    elif "member" in data:
        import aws_sdk_cleanrooms.types.protected_job_member_output_configuration_output

        return {
            "member": aws_sdk_cleanrooms.types.protected_job_member_output_configuration_output.deserialize_json(
                data["member"]
            )
        }
    else:
        raise DeserializationError(
            "ProtectedJobOutputConfigurationOutput: no recognized variant key"
        )
