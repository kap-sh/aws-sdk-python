"""Generated from Smithy shape ``com.amazonaws.connect#AssociatedContactSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.associated_contact_summary

AssociatedContactSummaryList: TypeAlias = list[
    "capo_connect.types.associated_contact_summary.AssociatedContactSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedContactSummaryList) -> list:
    import capo_connect.types.associated_contact_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.associated_contact_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedContactSummaryList:
    import capo_connect.types.associated_contact_summary

    out: AssociatedContactSummaryList = []
    for item in data:
        out.append(capo_connect.types.associated_contact_summary.deserialize_json(item))
    return out
