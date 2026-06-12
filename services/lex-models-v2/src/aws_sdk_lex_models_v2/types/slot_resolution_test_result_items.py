"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionTestResultItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.slot_resolution_test_result_item

SlotResolutionTestResultItems: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.slot_resolution_test_result_item.SlotResolutionTestResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotResolutionTestResultItems) -> list:
    import aws_sdk_lex_models_v2.types.slot_resolution_test_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.slot_resolution_test_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SlotResolutionTestResultItems:
    import aws_sdk_lex_models_v2.types.slot_resolution_test_result_item

    out: SlotResolutionTestResultItems = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.slot_resolution_test_result_item.deserialize_json(
                item
            )
        )
    return out
