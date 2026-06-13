"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#RelatedVulnerabilities``."""

from typing import TypeAlias

RelatedVulnerabilities: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedVulnerabilities) -> list:
    return list(value)


def deserialize_json(data: list) -> RelatedVulnerabilities:
    return list(data)
