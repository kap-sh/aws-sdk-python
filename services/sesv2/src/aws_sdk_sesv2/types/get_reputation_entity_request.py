"""Generated from Smithy shape ``com.amazonaws.sesv2#GetReputationEntityRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.reputation_entity_reference
    import aws_sdk_sesv2.types.reputation_entity_type


class GetReputationEntityRequest(TypedDict):
    reputation_entity_reference: (
        "aws_sdk_sesv2.types.reputation_entity_reference.ReputationEntityReference"
    )
    """<p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>"""
    reputation_entity_type: (
        "aws_sdk_sesv2.types.reputation_entity_type.ReputationEntityType"
    )
    """<p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReputationEntityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReputationEntityRequest:
    out: GetReputationEntityRequest = {}  # type: ignore[typeddict-item]
    return out
