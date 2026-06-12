"""Generated from Smithy shape ``com.amazonaws.connect#AssociatedContactSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.associated_contact_summary

AssociatedContactSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.associated_contact_summary.AssociatedContactSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedContactSummaryList) -> list:
    import aws_sdk_connect.types.associated_contact_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.associated_contact_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedContactSummaryList:
    import aws_sdk_connect.types.associated_contact_summary

    out: AssociatedContactSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.associated_contact_summary.deserialize_json(item)
        )
    return out
