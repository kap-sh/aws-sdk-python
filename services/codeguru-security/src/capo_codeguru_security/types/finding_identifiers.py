"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FindingIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_security.types.finding_identifier

FindingIdentifiers: TypeAlias = list[
    "capo_codeguru_security.types.finding_identifier.FindingIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingIdentifiers) -> list:
    import capo_codeguru_security.types.finding_identifier

    out: list = []
    for item in value:
        out.append(capo_codeguru_security.types.finding_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingIdentifiers:
    import capo_codeguru_security.types.finding_identifier

    out: FindingIdentifiers = []
    for item in data:
        out.append(
            capo_codeguru_security.types.finding_identifier.deserialize_json(item)
        )
    return out
