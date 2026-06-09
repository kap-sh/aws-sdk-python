"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionTermUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

EksAnywhereSubscriptionTermUnit: TypeAlias = Literal["MONTHS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MONTHS",))


def serialize_json(value: EksAnywhereSubscriptionTermUnit) -> str:
    return value


def deserialize_json(data: str) -> EksAnywhereSubscriptionTermUnit:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EksAnywhereSubscriptionTermUnit value: {data!r}"
        )
    return cast(EksAnywhereSubscriptionTermUnit, data)
