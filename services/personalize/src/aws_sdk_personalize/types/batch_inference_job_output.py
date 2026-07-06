"""Generated from Smithy shape ``com.amazonaws.personalize#BatchInferenceJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.s3_data_config


class BatchInferenceJobOutput(TypedDict, closed=True):
    s3_data_destination: "aws_sdk_personalize.types.s3_data_config.S3DataConfig"
    """<p>Information on the Amazon S3 bucket in which the batch inference job's output is stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchInferenceJobOutput) -> dict:
    out: dict = {}
    import aws_sdk_personalize.types.s3_data_config

    out["s3DataDestination"] = (
        aws_sdk_personalize.types.s3_data_config.serialize_aws_json_1_1(
            value["s3_data_destination"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchInferenceJobOutput:
    out: BatchInferenceJobOutput = {}  # type: ignore[typeddict-item]
    if "s3DataDestination" in data:
        import aws_sdk_personalize.types.s3_data_config

        out["s3_data_destination"] = (
            aws_sdk_personalize.types.s3_data_config.deserialize_aws_json_1_1(
                data["s3DataDestination"]
            )
        )
    else:
        raise DeserializationError(
            "BatchInferenceJobOutput.s3_data_destination required"
        )
    return out
