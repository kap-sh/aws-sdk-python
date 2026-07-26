"""Generated from Smithy shape ``com.amazonaws.datazone#DomainSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.domain_summary

DomainSummaries: TypeAlias = list["capo_datazone.types.domain_summary.DomainSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummaries) -> list:
    import capo_datazone.types.domain_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.domain_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainSummaries:
    import capo_datazone.types.domain_summary

    out: DomainSummaries = []
    for item in data:
        out.append(capo_datazone.types.domain_summary.deserialize_json(item))
    return out
