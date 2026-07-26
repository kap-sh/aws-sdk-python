"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociatedStandardsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.associated_standard

AssociatedStandardsList: TypeAlias = list[
    "capo_securityhub.types.associated_standard.AssociatedStandard"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedStandardsList) -> list:
    import capo_securityhub.types.associated_standard

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.associated_standard.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedStandardsList:
    import capo_securityhub.types.associated_standard

    out: AssociatedStandardsList = []
    for item in data:
        out.append(capo_securityhub.types.associated_standard.deserialize_json(item))
    return out
