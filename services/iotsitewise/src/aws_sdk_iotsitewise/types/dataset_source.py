"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.dataset_source_format
    import aws_sdk_iotsitewise.types.dataset_source_type
    import aws_sdk_iotsitewise.types.source_detail


class DatasetSource(TypedDict, closed=True):
    source_type: "aws_sdk_iotsitewise.types.dataset_source_type.DatasetSourceType"
    """<p>The type of data source for the dataset.</p>"""
    source_format: "aws_sdk_iotsitewise.types.dataset_source_format.DatasetSourceFormat"
    """<p>The format of the dataset source associated with the dataset.</p>"""
    source_detail: NotRequired["aws_sdk_iotsitewise.types.source_detail.SourceDetail"]
    """<p>The details of the dataset source associated with the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSource) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.dataset_source_type

    out["sourceType"] = aws_sdk_iotsitewise.types.dataset_source_type.serialize_json(
        value["source_type"]
    )
    import aws_sdk_iotsitewise.types.dataset_source_format

    out["sourceFormat"] = (
        aws_sdk_iotsitewise.types.dataset_source_format.serialize_json(
            value["source_format"]
        )
    )
    if "source_detail" in value:
        import aws_sdk_iotsitewise.types.source_detail

        out["sourceDetail"] = aws_sdk_iotsitewise.types.source_detail.serialize_json(
            value["source_detail"]
        )
    return out


def deserialize_json(data: dict) -> DatasetSource:
    out: DatasetSource = {}  # type: ignore[typeddict-item]
    if "sourceType" in data:
        import aws_sdk_iotsitewise.types.dataset_source_type

        out["source_type"] = (
            aws_sdk_iotsitewise.types.dataset_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        raise DeserializationError("DatasetSource.source_type required")
    if "sourceFormat" in data:
        import aws_sdk_iotsitewise.types.dataset_source_format

        out["source_format"] = (
            aws_sdk_iotsitewise.types.dataset_source_format.deserialize_json(
                data["sourceFormat"]
            )
        )
    else:
        raise DeserializationError("DatasetSource.source_format required")
    if "sourceDetail" in data:
        import aws_sdk_iotsitewise.types.source_detail

        out["source_detail"] = aws_sdk_iotsitewise.types.source_detail.deserialize_json(
            data["sourceDetail"]
        )
    return out
