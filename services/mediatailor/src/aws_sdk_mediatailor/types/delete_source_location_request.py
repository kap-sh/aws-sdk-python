"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteSourceLocationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeleteSourceLocationRequest(TypedDict):
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSourceLocationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSourceLocationRequest:
    out: DeleteSourceLocationRequest = {}  # type: ignore[typeddict-item]
    return out
