"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetSpaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string


class GetSpaceRequest(TypedDict):
    name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSpaceRequest:
    out: GetSpaceRequest = {}  # type: ignore[typeddict-item]
    return out
