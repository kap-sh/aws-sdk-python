"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DataModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.data_model
    import aws_sdk_timestream_write.types.data_model_s3_configuration


class DataModelConfiguration(TypedDict, closed=True):
    data_model: NotRequired["aws_sdk_timestream_write.types.data_model.DataModel"]
    """<p></p>"""
    data_model_s3_configuration: NotRequired[
        "aws_sdk_timestream_write.types.data_model_s3_configuration.DataModelS3Configuration"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataModelConfiguration) -> dict:
    out: dict = {}
    if "data_model" in value:
        import aws_sdk_timestream_write.types.data_model

        out["DataModel"] = (
            aws_sdk_timestream_write.types.data_model.serialize_aws_json_1_0(
                value["data_model"]
            )
        )
    if "data_model_s3_configuration" in value:
        import aws_sdk_timestream_write.types.data_model_s3_configuration

        out["DataModelS3Configuration"] = (
            aws_sdk_timestream_write.types.data_model_s3_configuration.serialize_aws_json_1_0(
                value["data_model_s3_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataModelConfiguration:
    out: DataModelConfiguration = {}  # type: ignore[typeddict-item]
    if "DataModel" in data:
        import aws_sdk_timestream_write.types.data_model

        out["data_model"] = (
            aws_sdk_timestream_write.types.data_model.deserialize_aws_json_1_0(
                data["DataModel"]
            )
        )
    if "DataModelS3Configuration" in data:
        import aws_sdk_timestream_write.types.data_model_s3_configuration

        out["data_model_s3_configuration"] = (
            aws_sdk_timestream_write.types.data_model_s3_configuration.deserialize_aws_json_1_0(
                data["DataModelS3Configuration"]
            )
        )
    return out
