"""Generated from Smithy shape ``com.amazonaws.qbusiness#HallucinationReductionControl``."""

from typing import Literal, TypeAlias, cast

HallucinationReductionControl: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HallucinationReductionControl) -> str:
    return value


def deserialize_json(data: str) -> HallucinationReductionControl:
    return cast(HallucinationReductionControl, data)
