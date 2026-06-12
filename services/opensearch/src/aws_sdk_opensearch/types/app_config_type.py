"""Generated from Smithy shape ``com.amazonaws.opensearch#AppConfigType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

AppConfigType: TypeAlias = Literal[
    "opensearchDashboards.dashboardAdmin.users",
    "opensearchDashboards.dashboardAdmin.groups",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "opensearchDashboards.dashboardAdmin.users",
        "opensearchDashboards.dashboardAdmin.groups",
    )
)


def serialize_json(value: AppConfigType) -> str:
    return value


def deserialize_json(data: str) -> AppConfigType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppConfigType value: {data!r}")
    return cast(AppConfigType, data)
