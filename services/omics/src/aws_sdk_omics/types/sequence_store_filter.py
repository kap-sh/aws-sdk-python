"""Generated from Smithy shape ``com.amazonaws.omics#SequenceStoreFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.sequence_store_name
    import aws_sdk_omics.types.sequence_store_status


class SequenceStoreFilter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>A name to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""
    status: NotRequired["aws_sdk_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>Filter results based on status.</p>"""
    updated_after: NotRequired["datetime.datetime"]
    """<p>Filter results based on stores updated after the specified time.</p>"""
    updated_before: NotRequired["datetime.datetime"]
    """<p>Filter results based on stores updated before the specified time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SequenceStoreFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "created_after" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["createdAfter"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["createdBefore"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["created_before"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "updated_after" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["updatedAfter"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["updated_after"]
        )
    if "updated_before" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["updatedBefore"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["updated_before"]
        )
    return out


def deserialize_json(data: dict) -> SequenceStoreFilter:
    out: SequenceStoreFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "createdAfter" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["created_after"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["createdAfter"]
        )
    if "createdBefore" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["created_before"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["createdBefore"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "updatedAfter" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["updated_after"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["updatedAfter"]
        )
    if "updatedBefore" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["updated_before"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["updatedBefore"]
        )
    return out
