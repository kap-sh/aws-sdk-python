"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfigurationDisabledFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AnonymousUserDashboardEmbeddingConfigurationDisabledFeature: TypeAlias = Literal[
    "SHARED_VIEW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHARED_VIEW",))


def serialize_json(
    value: AnonymousUserDashboardEmbeddingConfigurationDisabledFeature,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> AnonymousUserDashboardEmbeddingConfigurationDisabledFeature:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnonymousUserDashboardEmbeddingConfigurationDisabledFeature value: {data!r}"
        )
    return cast(AnonymousUserDashboardEmbeddingConfigurationDisabledFeature, data)
