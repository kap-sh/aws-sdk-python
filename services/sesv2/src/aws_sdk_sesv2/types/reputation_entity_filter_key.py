"""Generated from Smithy shape ``com.amazonaws.sesv2#ReputationEntityFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The filter key to use when listing reputation entities. This can be one of the following:</p> <ul> <li> <p> <code>ENTITY_TYPE</code> – Filter by entity type.</p> </li> <li> <p> <code>REPUTATION_IMPACT</code> – Filter by reputation impact level.</p> </li> <li> <p> <code>SENDING_STATUS</code> – Filter by aggregate sending status.</p> </li> <li> <p> <code>ENTITY_REFERENCE_PREFIX</code> – Filter by entity reference prefix.</p> </li> </ul>"""
ReputationEntityFilterKey: TypeAlias = Literal[
    "ENTITY_TYPE",
    "REPUTATION_IMPACT",
    "SENDING_STATUS",
    "ENTITY_REFERENCE_PREFIX",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReputationEntityFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ReputationEntityFilterKey:
    return cast(ReputationEntityFilterKey, data)
