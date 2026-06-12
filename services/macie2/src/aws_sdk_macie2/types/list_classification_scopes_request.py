"""Generated from Smithy shape ``com.amazonaws.macie2#ListClassificationScopesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class ListClassificationScopesRequest(TypedDict):
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the classification scope to retrieve the unique identifier for.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClassificationScopesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClassificationScopesRequest:
    out: ListClassificationScopesRequest = {}  # type: ignore[typeddict-item]
    return out
