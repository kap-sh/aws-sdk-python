"""Generated from Smithy shape ``com.amazonaws.quicksight#S3Source``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.input_column_list
    import aws_sdk_quicksight.types.upload_settings


class S3Source(TypedDict):
    data_source_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the data source.</p>"""
    upload_settings: NotRequired[
        "aws_sdk_quicksight.types.upload_settings.UploadSettings"
    ]
    """<p>Information about the format for the S3 source file or files.</p>"""
    input_columns: "aws_sdk_quicksight.types.input_column_list.InputColumnList"
    """<p>A physical table type for an S3 data source.</p> <note> <p>For files that aren't JSON, only <code>STRING</code> data types are supported in input columns.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Source) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    if "upload_settings" in value:
        import aws_sdk_quicksight.types.upload_settings

        out["UploadSettings"] = aws_sdk_quicksight.types.upload_settings.serialize_json(
            value["upload_settings"]
        )
    import aws_sdk_quicksight.types.input_column_list

    out["InputColumns"] = aws_sdk_quicksight.types.input_column_list.serialize_json(
        value["input_columns"]
    )
    return out


def deserialize_json(data: dict) -> S3Source:
    out: S3Source = {}  # type: ignore[typeddict-item]
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("S3Source.data_source_arn required")
    if "UploadSettings" in data:
        import aws_sdk_quicksight.types.upload_settings

        out["upload_settings"] = (
            aws_sdk_quicksight.types.upload_settings.deserialize_json(
                data["UploadSettings"]
            )
        )
    if "InputColumns" in data:
        import aws_sdk_quicksight.types.input_column_list

        out["input_columns"] = (
            aws_sdk_quicksight.types.input_column_list.deserialize_json(
                data["InputColumns"]
            )
        )
    else:
        raise DeserializationError("S3Source.input_columns required")
    return out
