"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfigurationEnabledFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AnonymousUserDashboardEmbeddingConfigurationEnabledFeature: TypeAlias = Literal[
    "SHARED_VIEW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHARED_VIEW",))


def serialize_json(
    value: AnonymousUserDashboardEmbeddingConfigurationEnabledFeature,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> AnonymousUserDashboardEmbeddingConfigurationEnabledFeature:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnonymousUserDashboardEmbeddingConfigurationEnabledFeature value: {data!r}"
        )
    return cast(AnonymousUserDashboardEmbeddingConfigurationEnabledFeature, data)
