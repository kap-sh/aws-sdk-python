"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_summary

DomainUnitSummaries: TypeAlias = list[
    "capo_datazone.types.domain_unit_summary.DomainUnitSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitSummaries) -> list:
    import capo_datazone.types.domain_unit_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.domain_unit_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainUnitSummaries:
    import capo_datazone.types.domain_unit_summary

    out: DomainUnitSummaries = []
    for item in data:
        out.append(capo_datazone.types.domain_unit_summary.deserialize_json(item))
    return out
