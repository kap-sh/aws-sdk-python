"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.service_summary

ServiceSummaries: TypeAlias = list[
    "capo_application_signals.types.service_summary.ServiceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSummaries) -> list:
    import capo_application_signals.types.service_summary

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.service_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceSummaries:
    import capo_application_signals.types.service_summary

    out: ServiceSummaries = []
    for item in data:
        out.append(
            capo_application_signals.types.service_summary.deserialize_json(item)
        )
    return out
