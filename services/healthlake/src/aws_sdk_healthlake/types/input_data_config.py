"""Generated from Smithy shape ``com.amazonaws.healthlake#InputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_healthlake.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.s3_uri


class _InputDataConfig_S3Uri(TypedDict):
    S3Uri: "aws_sdk_healthlake.types.s3_uri.S3Uri"


InputDataConfig: TypeAlias = _InputDataConfig_S3Uri


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputDataConfig) -> dict:
    if "S3Uri" in value:
        return {"S3Uri": value["S3Uri"]}
    else:
        raise SerializationError("InputDataConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> InputDataConfig:
    if "S3Uri" in data:
        return {"S3Uri": data["S3Uri"]}
    else:
        raise DeserializationError("InputDataConfig: no recognized variant key")
