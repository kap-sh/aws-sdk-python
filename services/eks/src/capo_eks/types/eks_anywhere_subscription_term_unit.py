"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionTermUnit``."""

from typing import Literal, TypeAlias, cast

EksAnywhereSubscriptionTermUnit: TypeAlias = Literal["MONTHS",]


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionTermUnit) -> str:
    return value


def deserialize_json(data: str) -> EksAnywhereSubscriptionTermUnit:
    return cast(EksAnywhereSubscriptionTermUnit, data)
