"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetIntentDiscrepancyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_item

TestSetIntentDiscrepancyList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_item.TestSetIntentDiscrepancyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetIntentDiscrepancyList) -> list:
    import aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TestSetIntentDiscrepancyList:
    import aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_item

    out: TestSetIntentDiscrepancyList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_item.deserialize_json(
                item
            )
        )
    return out
