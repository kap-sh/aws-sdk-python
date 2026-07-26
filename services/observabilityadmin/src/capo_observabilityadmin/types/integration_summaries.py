"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#IntegrationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.integration_summary

IntegrationSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.integration_summary.IntegrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummaries) -> list:
    import capo_observabilityadmin.types.integration_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.integration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegrationSummaries:
    import capo_observabilityadmin.types.integration_summary

    out: IntegrationSummaries = []
    for item in data:
        out.append(
            capo_observabilityadmin.types.integration_summary.deserialize_json(item)
        )
    return out
