"""Generated from Smithy shape ``com.amazonaws.healthlake#OutputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_healthlake.types.s3_configuration


class _OutputDataConfig_S3Configuration(TypedDict, closed=True):
    S3Configuration: "capo_healthlake.types.s3_configuration.S3Configuration"


OutputDataConfig: TypeAlias = _OutputDataConfig_S3Configuration


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputDataConfig) -> dict:
    if "S3Configuration" in value:
        import capo_healthlake.types.s3_configuration

        return {
            "S3Configuration": capo_healthlake.types.s3_configuration.serialize_aws_json_1_0(
                value["S3Configuration"]
            )
        }
    else:
        raise SerializationError("OutputDataConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> OutputDataConfig:
    if "S3Configuration" in data:
        import capo_healthlake.types.s3_configuration

        return {
            "S3Configuration": capo_healthlake.types.s3_configuration.deserialize_aws_json_1_0(
                data["S3Configuration"]
            )
        }
    else:
        raise DeserializationError("OutputDataConfig: no recognized variant key")
