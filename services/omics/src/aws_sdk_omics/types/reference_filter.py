"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.md5
    import aws_sdk_omics.types.reference_name


class ReferenceFilter(TypedDict):
    name: NotRequired["aws_sdk_omics.types.reference_name.ReferenceName"]
    """<p>A name to filter on.</p>"""
    md5: NotRequired["aws_sdk_omics.types.md5.Md5"]
    """<p>An MD5 checksum to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "md5" in value:
        out["md5"] = value["md5"]
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


def deserialize_json(data: dict) -> ReferenceFilter:
    out: ReferenceFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "md5" in data:
        out["md5"] = data["md5"]
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
