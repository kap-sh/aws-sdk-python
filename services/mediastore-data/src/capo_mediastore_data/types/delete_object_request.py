"""Generated from Smithy shape ``com.amazonaws.mediastoredata#DeleteObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore_data.types.path_naming


class DeleteObjectRequest(TypedDict, closed=True):
    path: "capo_mediastore_data.types.path_naming.PathNaming"
    """<p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteObjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteObjectRequest:
    out: DeleteObjectRequest = {}  # type: ignore[typeddict-item]
    return out
