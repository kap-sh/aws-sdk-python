"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SuggestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.query
    import aws_sdk_cloudsearch_domain.types.suggester
    import aws_sdk_cloudsearch_domain.types.suggestions_size


class SuggestRequest(TypedDict, closed=True):
    query: "aws_sdk_cloudsearch_domain.types.query.Query"
    """<p>Specifies the string for which you want to get suggestions.</p>"""
    suggester: "aws_sdk_cloudsearch_domain.types.suggester.Suggester"
    """<p>Specifies the name of the suggester to use to find suggested matches.</p>"""
    size: "aws_sdk_cloudsearch_domain.types.suggestions_size.SuggestionsSize"
    """<p>Specifies the maximum number of suggestions to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SuggestRequest:
    out: SuggestRequest = {}  # type: ignore[typeddict-item]
    return out
