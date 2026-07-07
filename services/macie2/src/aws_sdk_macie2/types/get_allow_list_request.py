"""Generated from Smithy shape ``com.amazonaws.macie2#GetAllowListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class GetAllowListRequest(TypedDict, closed=True):
    id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAllowListRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAllowListRequest:
    out: GetAllowListRequest = {}  # type: ignore[typeddict-item]
    return out
