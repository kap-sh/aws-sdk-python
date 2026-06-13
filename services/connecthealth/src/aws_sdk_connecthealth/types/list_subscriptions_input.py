"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListSubscriptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id


class ListSubscriptionsInput(TypedDict):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return.</p>"""
    next_token: NotRequired["str"]
    """<p>Token for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionsInput:
    out: ListSubscriptionsInput = {}  # type: ignore[typeddict-item]
    return out
