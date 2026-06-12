"""Generated from Smithy shape ``com.amazonaws.polly#ListLexiconsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_polly.types.next_token


class ListLexiconsInput(TypedDict):
    next_token: NotRequired["aws_sdk_polly.types.next_token.NextToken"]
    """<p>An opaque pagination token returned from previous <code>ListLexicons</code> operation. If present, indicates where to continue the list of lexicons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLexiconsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLexiconsInput:
    out: ListLexiconsInput = {}  # type: ignore[typeddict-item]
    return out
