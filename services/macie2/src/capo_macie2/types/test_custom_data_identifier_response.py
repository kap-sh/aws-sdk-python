"""Generated from Smithy shape ``com.amazonaws.macie2#TestCustomDataIdentifierResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__integer


class TestCustomDataIdentifierResponse(TypedDict, closed=True):
    match_count: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The number of occurrences of sample text that matched the criteria specified by the custom data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCustomDataIdentifierResponse) -> dict:
    out: dict = {}
    if "match_count" in value:
        out["matchCount"] = value["match_count"]
    return out


def deserialize_json(data: dict) -> TestCustomDataIdentifierResponse:
    out: TestCustomDataIdentifierResponse = {}  # type: ignore[typeddict-item]
    if "matchCount" in data:
        out["match_count"] = data["matchCount"]
    return out
