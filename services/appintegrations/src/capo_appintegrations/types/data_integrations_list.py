"""Generated from Smithy shape ``com.amazonaws.appintegrations#DataIntegrationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appintegrations.types.data_integration_summary

DataIntegrationsList: TypeAlias = list[
    "capo_appintegrations.types.data_integration_summary.DataIntegrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationsList) -> list:
    import capo_appintegrations.types.data_integration_summary

    out: list = []
    for item in value:
        out.append(
            capo_appintegrations.types.data_integration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataIntegrationsList:
    import capo_appintegrations.types.data_integration_summary

    out: DataIntegrationsList = []
    for item in data:
        out.append(
            capo_appintegrations.types.data_integration_summary.deserialize_json(item)
        )
    return out
