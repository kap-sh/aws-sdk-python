"""Generated from Smithy shape ``com.amazonaws.acmpca#KeyStorageSecurityStandard``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

KeyStorageSecurityStandard: TypeAlias = Literal[
    "FIPS_140_2_LEVEL_2_OR_HIGHER",
    "FIPS_140_2_LEVEL_3_OR_HIGHER",
    "CCPC_LEVEL_1_OR_HIGHER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIPS_140_2_LEVEL_2_OR_HIGHER",
        "FIPS_140_2_LEVEL_3_OR_HIGHER",
        "CCPC_LEVEL_1_OR_HIGHER",
    )
)


def serialize_aws_json_1_1(value: KeyStorageSecurityStandard) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyStorageSecurityStandard:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KeyStorageSecurityStandard value: {data!r}"
        )
    return cast(KeyStorageSecurityStandard, data)
