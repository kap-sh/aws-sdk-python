"""Generated from Smithy shape ``com.amazonaws.kendra#ExpandedResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.expanded_result_item

ExpandedResultList: TypeAlias = list[
    "capo_kendra.types.expanded_result_item.ExpandedResultItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpandedResultList) -> list:
    import capo_kendra.types.expanded_result_item

    out: list = []
    for item in value:
        out.append(capo_kendra.types.expanded_result_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExpandedResultList:
    import capo_kendra.types.expanded_result_item

    out: ExpandedResultList = []
    for item in data:
        out.append(
            capo_kendra.types.expanded_result_item.deserialize_aws_json_1_1(item)
        )
    return out
