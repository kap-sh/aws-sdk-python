"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionLicenseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

EksAnywhereSubscriptionLicenseType: TypeAlias = Literal["Cluster",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Cluster",))


def serialize_json(value: EksAnywhereSubscriptionLicenseType) -> str:
    return value


def deserialize_json(data: str) -> EksAnywhereSubscriptionLicenseType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EksAnywhereSubscriptionLicenseType value: {data!r}"
        )
    return cast(EksAnywhereSubscriptionLicenseType, data)
