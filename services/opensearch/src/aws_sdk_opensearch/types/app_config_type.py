"""Generated from Smithy shape ``com.amazonaws.opensearch#AppConfigType``."""

from typing import Literal, TypeAlias, cast

AppConfigType: TypeAlias = Literal[
    "opensearchDashboards.dashboardAdmin.users",
    "opensearchDashboards.dashboardAdmin.groups",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppConfigType) -> str:
    return value


def deserialize_json(data: str) -> AppConfigType:
    return cast(AppConfigType, data)
