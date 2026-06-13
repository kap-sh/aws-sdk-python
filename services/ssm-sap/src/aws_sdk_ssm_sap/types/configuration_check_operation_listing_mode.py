"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckOperationListingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ConfigurationCheckOperationListingMode: TypeAlias = Literal[
    "ALL_OPERATIONS",
    "LATEST_PER_CHECK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_OPERATIONS",
        "LATEST_PER_CHECK",
    )
)


def serialize_json(value: ConfigurationCheckOperationListingMode) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationCheckOperationListingMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurationCheckOperationListingMode value: {data!r}"
        )
    return cast(ConfigurationCheckOperationListingMode, data)
