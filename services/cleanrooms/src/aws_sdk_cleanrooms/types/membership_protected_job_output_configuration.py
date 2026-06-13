"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipProtectedJobOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_input


class _MembershipProtectedJobOutputConfiguration_s3(TypedDict):
    s3: "aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_input.ProtectedJobS3OutputConfigurationInput"


MembershipProtectedJobOutputConfiguration: TypeAlias = (
    _MembershipProtectedJobOutputConfiguration_s3
)


# --- restJson1 ser/de ---
def serialize_json(value: MembershipProtectedJobOutputConfiguration) -> dict:
    if "s3" in value:
        import aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_input

        return {
            "s3": aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_input.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError(
            "MembershipProtectedJobOutputConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MembershipProtectedJobOutputConfiguration:
    if "s3" in data:
        import aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_input

        return {
            "s3": aws_sdk_cleanrooms.types.protected_job_s3_output_configuration_input.deserialize_json(
                data["s3"]
            )
        }
    else:
        raise DeserializationError(
            "MembershipProtectedJobOutputConfiguration: no recognized variant key"
        )
