"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricsStatus``."""

from typing import Literal, TypeAlias, cast

MetricsStatus: TypeAlias = Literal[
    "PUBLISH_SUCCEEDED",
    "PUBLISH_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricsStatus) -> str:
    return value


def deserialize_json(data: str) -> MetricsStatus:
    return cast(MetricsStatus, data)
