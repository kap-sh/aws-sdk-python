"""Generated from Smithy shape ``com.amazonaws.iot#ConfirmTopicRuleDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.confirmation_token


class ConfirmTopicRuleDestinationRequest(TypedDict, closed=True):
    confirmation_token: "capo_iot.types.confirmation_token.ConfirmationToken"
    """<p>The token used to confirm ownership or access to the topic rule confirmation URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfirmTopicRuleDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ConfirmTopicRuleDestinationRequest:
    out: ConfirmTopicRuleDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
