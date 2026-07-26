"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class DeleteDirectoryRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDirectoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDirectoryRequest:
    out: DeleteDirectoryRequest = {}  # type: ignore[typeddict-item]
    return out
