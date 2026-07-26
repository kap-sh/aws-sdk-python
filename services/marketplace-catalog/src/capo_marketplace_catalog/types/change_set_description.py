"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ChangeSetDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.change_summary

ChangeSetDescription: TypeAlias = list[
    "capo_marketplace_catalog.types.change_summary.ChangeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSetDescription) -> list:
    import capo_marketplace_catalog.types.change_summary

    out: list = []
    for item in value:
        out.append(capo_marketplace_catalog.types.change_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeSetDescription:
    import capo_marketplace_catalog.types.change_summary

    out: ChangeSetDescription = []
    for item in data:
        out.append(capo_marketplace_catalog.types.change_summary.deserialize_json(item))
    return out
