"""Generated from Smithy shape ``com.amazonaws.quicksight#S3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.input_column_list
    import capo_quicksight.types.upload_settings


class S3Source(TypedDict, closed=True):
    data_source_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the data source.</p>"""
    upload_settings: NotRequired["capo_quicksight.types.upload_settings.UploadSettings"]
    """<p>Information about the format for the S3 source file or files.</p>"""
    input_columns: "capo_quicksight.types.input_column_list.InputColumnList"
    """<p>A physical table type for an S3 data source.</p> <note> <p>For files that aren't JSON, only <code>STRING</code> data types are supported in input columns.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Source) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    if "upload_settings" in value:
        import capo_quicksight.types.upload_settings

        out["UploadSettings"] = capo_quicksight.types.upload_settings.serialize_json(
            value["upload_settings"]
        )
    import capo_quicksight.types.input_column_list

    out["InputColumns"] = capo_quicksight.types.input_column_list.serialize_json(
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
        import capo_quicksight.types.upload_settings

        out["upload_settings"] = capo_quicksight.types.upload_settings.deserialize_json(
            data["UploadSettings"]
        )
    if "InputColumns" in data:
        import capo_quicksight.types.input_column_list

        out["input_columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["InputColumns"]
        )
    else:
        raise DeserializationError("S3Source.input_columns required")
    return out
