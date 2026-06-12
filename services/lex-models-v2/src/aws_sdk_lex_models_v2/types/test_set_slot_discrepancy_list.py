"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetSlotDiscrepancyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_item

TestSetSlotDiscrepancyList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_item.TestSetSlotDiscrepancyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetSlotDiscrepancyList) -> list:
    import aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TestSetSlotDiscrepancyList:
    import aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_item

    out: TestSetSlotDiscrepancyList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_item.deserialize_json(
                item
            )
        )
    return out
