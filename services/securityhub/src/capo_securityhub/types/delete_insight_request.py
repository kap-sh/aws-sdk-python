"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class DeleteInsightRequest(TypedDict, closed=True):
    insight_arn: "capo_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the insight to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInsightRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInsightRequest:
    out: DeleteInsightRequest = {}  # type: ignore[typeddict-item]
    return out
