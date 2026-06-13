"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_unit_summary

DomainUnitSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.domain_unit_summary.DomainUnitSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitSummaries) -> list:
    import aws_sdk_datazone.types.domain_unit_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.domain_unit_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainUnitSummaries:
    import aws_sdk_datazone.types.domain_unit_summary

    out: DomainUnitSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.domain_unit_summary.deserialize_json(item))
    return out
