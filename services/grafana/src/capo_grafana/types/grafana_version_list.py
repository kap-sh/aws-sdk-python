"""Generated from Smithy shape ``com.amazonaws.grafana#GrafanaVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.grafana_version

GrafanaVersionList: TypeAlias = list[
    "capo_grafana.types.grafana_version.GrafanaVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: GrafanaVersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> GrafanaVersionList:
    return list(data)
