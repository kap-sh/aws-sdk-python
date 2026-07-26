"""Generated from Smithy shape ``com.amazonaws.kendra#ConflictingItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.conflicting_item

ConflictingItems: TypeAlias = list["capo_kendra.types.conflicting_item.ConflictingItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictingItems) -> list:
    import capo_kendra.types.conflicting_item

    out: list = []
    for item in value:
        out.append(capo_kendra.types.conflicting_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConflictingItems:
    import capo_kendra.types.conflicting_item

    out: ConflictingItems = []
    for item in data:
        out.append(capo_kendra.types.conflicting_item.deserialize_aws_json_1_1(item))
    return out
