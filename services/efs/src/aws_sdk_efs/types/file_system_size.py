"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemSize``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_nullable_size_value
    import aws_sdk_efs.types.file_system_size_value
    import aws_sdk_efs.types.timestamp


class FileSystemSize(TypedDict, closed=True):
    value: "aws_sdk_efs.types.file_system_size_value.FileSystemSizeValue"
    """<p>The latest known metered size (in bytes) of data stored in the file system.</p>"""
    timestamp: NotRequired["aws_sdk_efs.types.timestamp.Timestamp"]
    """<p>The time at which the size of data, returned in the <code>Value</code> field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.</p>"""
    value_in_ia: NotRequired[
        "aws_sdk_efs.types.file_system_nullable_size_value.FileSystemNullableSizeValue"
    ]
    """<p>The latest known metered size (in bytes) of data stored in the Infrequent Access storage class.</p>"""
    value_in_standard: NotRequired[
        "aws_sdk_efs.types.file_system_nullable_size_value.FileSystemNullableSizeValue"
    ]
    """<p>The latest known metered size (in bytes) of data stored in the Standard storage class.</p>"""
    value_in_archive: NotRequired[
        "aws_sdk_efs.types.file_system_nullable_size_value.FileSystemNullableSizeValue"
    ]
    """<p>The latest known metered size (in bytes) of data stored in the Archive storage class.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemSize) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", 0)
    if "timestamp" in value:
        import aws_sdk_efs.types.timestamp

        out["Timestamp"] = aws_sdk_efs.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "value_in_ia" in value:
        out["ValueInIA"] = value["value_in_ia"]
    if "value_in_standard" in value:
        out["ValueInStandard"] = value["value_in_standard"]
    if "value_in_archive" in value:
        out["ValueInArchive"] = value["value_in_archive"]
    return out


def deserialize_json(data: dict) -> FileSystemSize:
    out: FileSystemSize = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if "Timestamp" in data:
        import aws_sdk_efs.types.timestamp

        out["timestamp"] = aws_sdk_efs.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "ValueInIA" in data:
        out["value_in_ia"] = data["ValueInIA"]
    if "ValueInStandard" in data:
        out["value_in_standard"] = data["ValueInStandard"]
    if "ValueInArchive" in data:
        out["value_in_archive"] = data["ValueInArchive"]
    return out
