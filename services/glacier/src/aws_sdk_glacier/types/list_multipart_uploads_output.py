"""Generated from Smithy shape ``com.amazonaws.glacier#ListMultipartUploadsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string
    import aws_sdk_glacier.types.uploads_list


class ListMultipartUploadsOutput(TypedDict):
    uploads_list: NotRequired["aws_sdk_glacier.types.uploads_list.UploadsList"]
    """<p>A list of in-progress multipart uploads.</p>"""
    marker: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>An opaque string that represents where to continue pagination of the results. You use the marker in a new List Multipart Uploads request to obtain more uploads in the list. If there are no more uploads, this value is <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultipartUploadsOutput) -> dict:
    out: dict = {}
    if "uploads_list" in value:
        import aws_sdk_glacier.types.uploads_list

        out["UploadsList"] = aws_sdk_glacier.types.uploads_list.serialize_json(
            value["uploads_list"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> ListMultipartUploadsOutput:
    out: ListMultipartUploadsOutput = {}  # type: ignore[typeddict-item]
    if "UploadsList" in data:
        import aws_sdk_glacier.types.uploads_list

        out["uploads_list"] = aws_sdk_glacier.types.uploads_list.deserialize_json(
            data["UploadsList"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
