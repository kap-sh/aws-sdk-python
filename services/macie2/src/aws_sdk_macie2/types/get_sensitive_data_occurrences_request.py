"""Generated from Smithy shape ``com.amazonaws.macie2#GetSensitiveDataOccurrencesRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class GetSensitiveDataOccurrencesRequest(TypedDict):
    finding_id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSensitiveDataOccurrencesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSensitiveDataOccurrencesRequest:
    out: GetSensitiveDataOccurrencesRequest = {}  # type: ignore[typeddict-item]
    return out
