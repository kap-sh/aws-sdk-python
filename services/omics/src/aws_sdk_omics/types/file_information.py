"""Generated from Smithy shape ``com.amazonaws.omics#FileInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_s3_access


class FileInformation(TypedDict, closed=True):
    total_parts: NotRequired["int"]
    """<p>The file's total parts.</p>"""
    part_size: NotRequired["int"]
    """<p>The file's part size.</p>"""
    content_length: NotRequired["int"]
    """<p>The file's content length.</p>"""
    s3_access: NotRequired["aws_sdk_omics.types.read_set_s3_access.ReadSetS3Access"]
    """<p>The S3 URI metadata of a sequence store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileInformation) -> dict:
    out: dict = {}
    if "total_parts" in value:
        out["totalParts"] = value["total_parts"]
    if "part_size" in value:
        out["partSize"] = value["part_size"]
    if "content_length" in value:
        out["contentLength"] = value["content_length"]
    if "s3_access" in value:
        import aws_sdk_omics.types.read_set_s3_access

        out["s3Access"] = aws_sdk_omics.types.read_set_s3_access.serialize_json(
            value["s3_access"]
        )
    return out


def deserialize_json(data: dict) -> FileInformation:
    out: FileInformation = {}  # type: ignore[typeddict-item]
    if "totalParts" in data:
        out["total_parts"] = data["totalParts"]
    if "partSize" in data:
        out["part_size"] = data["partSize"]
    if "contentLength" in data:
        out["content_length"] = data["contentLength"]
    if "s3Access" in data:
        import aws_sdk_omics.types.read_set_s3_access

        out["s3_access"] = aws_sdk_omics.types.read_set_s3_access.deserialize_json(
            data["s3Access"]
        )
    return out
