"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteSpaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string


class DeleteSpaceRequest(TypedDict, closed=True):
    name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space. To retrieve a list of space names, use <a>ListSpaces</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSpaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSpaceRequest:
    out: DeleteSpaceRequest = {}  # type: ignore[typeddict-item]
    return out
