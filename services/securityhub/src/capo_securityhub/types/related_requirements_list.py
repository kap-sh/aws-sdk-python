"""Generated from Smithy shape ``com.amazonaws.securityhub#RelatedRequirementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string

RelatedRequirementsList: TypeAlias = list[
    "capo_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedRequirementsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RelatedRequirementsList:
    return list(data)
