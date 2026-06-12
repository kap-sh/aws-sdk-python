"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

DatasourcePackage: TypeAlias = Literal[
    "DETECTIVE_CORE",
    "EKS_AUDIT",
    "ASFF_SECURITYHUB_FINDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DETECTIVE_CORE",
        "EKS_AUDIT",
        "ASFF_SECURITYHUB_FINDING",
    )
)


def serialize_json(value: DatasourcePackage) -> str:
    return value


def deserialize_json(data: str) -> DatasourcePackage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasourcePackage value: {data!r}")
    return cast(DatasourcePackage, data)
