"""Generated from Smithy shape ``com.amazonaws.glacier#ListMultipartUploadsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string
    import capo_glacier.types.uploads_list


class ListMultipartUploadsOutput(TypedDict, closed=True):
    uploads_list: NotRequired["capo_glacier.types.uploads_list.UploadsList"]
    """<p>A list of in-progress multipart uploads.</p>"""
    marker: NotRequired["capo_glacier.types.string.string"]
    """<p>An opaque string that represents where to continue pagination of the results. You use the marker in a new List Multipart Uploads request to obtain more uploads in the list. If there are no more uploads, this value is <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultipartUploadsOutput) -> dict:
    out: dict = {}
    if "uploads_list" in value:
        import capo_glacier.types.uploads_list

        out["UploadsList"] = capo_glacier.types.uploads_list.serialize_json(
            value["uploads_list"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> ListMultipartUploadsOutput:
    out: ListMultipartUploadsOutput = {}  # type: ignore[typeddict-item]
    if "UploadsList" in data:
        import capo_glacier.types.uploads_list

        out["uploads_list"] = capo_glacier.types.uploads_list.deserialize_json(
            data["UploadsList"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
