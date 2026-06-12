"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfFindingsFilterListItem``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.findings_filter_list_item

__listOfFindingsFilterListItem: TypeAlias = list[
    "aws_sdk_macie2.types.findings_filter_list_item.FindingsFilterListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFindingsFilterListItem) -> list:
    import aws_sdk_macie2.types.findings_filter_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.findings_filter_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFindingsFilterListItem:
    import aws_sdk_macie2.types.findings_filter_list_item

    out: __listOfFindingsFilterListItem = []
    for item in data:
        out.append(
            aws_sdk_macie2.types.findings_filter_list_item.deserialize_json(item)
        )
    return out
