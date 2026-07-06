"""Generated from Smithy shape ``com.amazonaws.databrew#FilesLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.max_files
    import aws_sdk_databrew.types.order
    import aws_sdk_databrew.types.ordered_by


class FilesLimit(TypedDict, closed=True):
    max_files: "aws_sdk_databrew.types.max_files.MaxFiles"
    """<p>The number of Amazon S3 files to select.</p>"""
    ordered_by: NotRequired["aws_sdk_databrew.types.ordered_by.OrderedBy"]
    """<p>A criteria to use for Amazon S3 files sorting before their selection. By default uses LAST_MODIFIED_DATE as a sorting criteria. Currently it's the only allowed value.</p>"""
    order: NotRequired["aws_sdk_databrew.types.order.Order"]
    """<p>A criteria to use for Amazon S3 files sorting before their selection. By default uses DESCENDING order, i.e. most recent files are selected first. Another possible value is ASCENDING.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilesLimit) -> dict:
    out: dict = {}
    out["MaxFiles"] = value["max_files"]
    if "ordered_by" in value:
        import aws_sdk_databrew.types.ordered_by

        out["OrderedBy"] = aws_sdk_databrew.types.ordered_by.serialize_json(
            value["ordered_by"]
        )
    if "order" in value:
        import aws_sdk_databrew.types.order

        out["Order"] = aws_sdk_databrew.types.order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> FilesLimit:
    out: FilesLimit = {}  # type: ignore[typeddict-item]
    if "MaxFiles" in data:
        out["max_files"] = data["MaxFiles"]
    else:
        raise DeserializationError("FilesLimit.max_files required")
    if "OrderedBy" in data:
        import aws_sdk_databrew.types.ordered_by

        out["ordered_by"] = aws_sdk_databrew.types.ordered_by.deserialize_json(
            data["OrderedBy"]
        )
    if "Order" in data:
        import aws_sdk_databrew.types.order

        out["order"] = aws_sdk_databrew.types.order.deserialize_json(data["Order"])
    return out
