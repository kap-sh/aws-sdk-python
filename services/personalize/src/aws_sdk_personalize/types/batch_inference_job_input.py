"""Generated from Smithy shape ``com.amazonaws.personalize#BatchInferenceJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.s3_data_config


class BatchInferenceJobInput(TypedDict):
    s3_data_source: "aws_sdk_personalize.types.s3_data_config.S3DataConfig"
    """<p>The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be in the same region as the API endpoint you are calling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchInferenceJobInput) -> dict:
    out: dict = {}
    import aws_sdk_personalize.types.s3_data_config

    out["s3DataSource"] = (
        aws_sdk_personalize.types.s3_data_config.serialize_aws_json_1_1(
            value["s3_data_source"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchInferenceJobInput:
    out: BatchInferenceJobInput = {}  # type: ignore[typeddict-item]
    if "s3DataSource" in data:
        import aws_sdk_personalize.types.s3_data_config

        out["s3_data_source"] = (
            aws_sdk_personalize.types.s3_data_config.deserialize_aws_json_1_1(
                data["s3DataSource"]
            )
        )
    else:
        raise DeserializationError("BatchInferenceJobInput.s3_data_source required")
    return out
