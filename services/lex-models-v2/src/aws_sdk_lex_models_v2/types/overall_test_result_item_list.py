"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OverallTestResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.overall_test_result_item

OverallTestResultItemList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.overall_test_result_item.OverallTestResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: OverallTestResultItemList) -> list:
    import aws_sdk_lex_models_v2.types.overall_test_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.overall_test_result_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OverallTestResultItemList:
    import aws_sdk_lex_models_v2.types.overall_test_result_item

    out: OverallTestResultItemList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.overall_test_result_item.deserialize_json(item)
        )
    return out
