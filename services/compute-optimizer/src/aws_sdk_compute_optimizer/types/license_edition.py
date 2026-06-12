"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseEdition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LicenseEdition: TypeAlias = Literal[
    "Enterprise",
    "Standard",
    "Free",
    "NoLicenseEditionFound",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enterprise",
        "Standard",
        "Free",
        "NoLicenseEditionFound",
    )
)


def serialize_aws_json_1_0(value: LicenseEdition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseEdition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseEdition value: {data!r}")
    return cast(LicenseEdition, data)
