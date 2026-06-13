"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_summary

ServiceSummaries: TypeAlias = list[
    "aws_sdk_application_signals.types.service_summary.ServiceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSummaries) -> list:
    import aws_sdk_application_signals.types.service_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.service_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceSummaries:
    import aws_sdk_application_signals.types.service_summary

    out: ServiceSummaries = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_summary.deserialize_json(item)
        )
    return out
