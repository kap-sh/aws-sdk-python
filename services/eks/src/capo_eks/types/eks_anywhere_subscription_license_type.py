"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionLicenseType``."""

from typing import Literal, TypeAlias, cast

EksAnywhereSubscriptionLicenseType: TypeAlias = Literal["Cluster",]


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionLicenseType) -> str:
    return value


def deserialize_json(data: str) -> EksAnywhereSubscriptionLicenseType:
    return cast(EksAnywhereSubscriptionLicenseType, data)
