"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetExportJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.s3_data_config


class DatasetExportJobOutput(TypedDict):
    s3_data_destination: "aws_sdk_personalize.types.s3_data_config.S3DataConfig"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetExportJobOutput) -> dict:
    out: dict = {}
    import aws_sdk_personalize.types.s3_data_config

    out["s3DataDestination"] = (
        aws_sdk_personalize.types.s3_data_config.serialize_aws_json_1_1(
            value["s3_data_destination"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetExportJobOutput:
    out: DatasetExportJobOutput = {}  # type: ignore[typeddict-item]
    if "s3DataDestination" in data:
        import aws_sdk_personalize.types.s3_data_config

        out["s3_data_destination"] = (
            aws_sdk_personalize.types.s3_data_config.deserialize_aws_json_1_1(
                data["s3DataDestination"]
            )
        )
    else:
        raise DeserializationError(
            "DatasetExportJobOutput.s3_data_destination required"
        )
    return out
