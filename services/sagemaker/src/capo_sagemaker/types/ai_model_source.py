"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIModelSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_model_source_s3


class _AIModelSource_S3(TypedDict, closed=True):
    S3: "capo_sagemaker.types.ai_model_source_s3.AIModelSourceS3"


AIModelSource: TypeAlias = _AIModelSource_S3


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIModelSource) -> dict:
    if "S3" in value:
        import capo_sagemaker.types.ai_model_source_s3

        return {
            "S3": capo_sagemaker.types.ai_model_source_s3.serialize_aws_json_1_1(
                value["S3"]
            )
        }
    else:
        raise SerializationError("AIModelSource: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AIModelSource:
    if "S3" in data:
        import capo_sagemaker.types.ai_model_source_s3

        return {
            "S3": capo_sagemaker.types.ai_model_source_s3.deserialize_aws_json_1_1(
                data["S3"]
            )
        }
    else:
        raise DeserializationError("AIModelSource: no recognized variant key")
