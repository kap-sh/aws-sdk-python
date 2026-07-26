"""Generated from Smithy shape ``com.amazonaws.inspector2#RelatedVulnerabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.related_vulnerability

RelatedVulnerabilities: TypeAlias = list[
    "capo_inspector2.types.related_vulnerability.RelatedVulnerability"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedVulnerabilities) -> list:
    return list(value)


def deserialize_json(data: list) -> RelatedVulnerabilities:
    return list(data)
