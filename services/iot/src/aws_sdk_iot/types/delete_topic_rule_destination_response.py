"""Generated from Smithy shape ``com.amazonaws.iot#DeleteTopicRuleDestinationResponse``."""

from typing_extensions import TypedDict


class DeleteTopicRuleDestinationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTopicRuleDestinationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTopicRuleDestinationResponse:
    out: DeleteTopicRuleDestinationResponse = {}  # type: ignore[typeddict-item]
    return out
