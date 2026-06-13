"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetUploadPartListFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime


class ReadSetUploadPartListFilter(TypedDict):
    created_after: NotRequired["datetime.datetime"]
    """<p> Filters for read set uploads after a specified time. </p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p> Filters for read set part uploads before a specified time. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetUploadPartListFilter) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> ReadSetUploadPartListFilter:
    out: ReadSetUploadPartListFilter = {}  # type: ignore[typeddict-item]
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
    return out
