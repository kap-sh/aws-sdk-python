"""Generated from Smithy shape ``com.amazonaws.kafka#RebalancingStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Intelligent rebalancing status. The default intelligent rebalancing status is ACTIVE for all new Express-based clusters.</p>"""
RebalancingStatus: TypeAlias = Literal[
    "PAUSED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RebalancingStatus) -> str:
    return value


def deserialize_json(data: str) -> RebalancingStatus:
    return cast(RebalancingStatus, data)
