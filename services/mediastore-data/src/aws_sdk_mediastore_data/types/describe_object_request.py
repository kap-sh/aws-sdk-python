"""Generated from Smithy shape ``com.amazonaws.mediastoredata#DescribeObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediastore_data.types.path_naming


class DescribeObjectRequest(TypedDict, closed=True):
    path: "aws_sdk_mediastore_data.types.path_naming.PathNaming"
    """<p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeObjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeObjectRequest:
    out: DescribeObjectRequest = {}  # type: ignore[typeddict-item]
    return out
