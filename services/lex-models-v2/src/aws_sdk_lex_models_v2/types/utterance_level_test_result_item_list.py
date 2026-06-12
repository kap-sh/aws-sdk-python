"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceLevelTestResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.utterance_level_test_result_item

UtteranceLevelTestResultItemList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.utterance_level_test_result_item.UtteranceLevelTestResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceLevelTestResultItemList) -> list:
    import aws_sdk_lex_models_v2.types.utterance_level_test_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.utterance_level_test_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UtteranceLevelTestResultItemList:
    import aws_sdk_lex_models_v2.types.utterance_level_test_result_item

    out: UtteranceLevelTestResultItemList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.utterance_level_test_result_item.deserialize_json(
                item
            )
        )
    return out
