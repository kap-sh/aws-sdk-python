"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AdditionalResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.additional_resources

AdditionalResourcesList: TypeAlias = list[
    "capo_wellarchitected.types.additional_resources.AdditionalResources"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalResourcesList) -> list:
    import capo_wellarchitected.types.additional_resources

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.additional_resources.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdditionalResourcesList:
    import capo_wellarchitected.types.additional_resources

    out: AdditionalResourcesList = []
    for item in data:
        out.append(
            capo_wellarchitected.types.additional_resources.deserialize_json(item)
        )
    return out
