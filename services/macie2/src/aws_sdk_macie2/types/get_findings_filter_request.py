"""Generated from Smithy shape ``com.amazonaws.macie2#GetFindingsFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class GetFindingsFilterRequest(TypedDict):
    id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsFilterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFindingsFilterRequest:
    out: GetFindingsFilterRequest = {}  # type: ignore[typeddict-item]
    return out
