"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetTurnRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.test_set_turn_record

TestSetTurnRecordList: TypeAlias = list[
    "capo_lex_models_v2.types.test_set_turn_record.TestSetTurnRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetTurnRecordList) -> list:
    import capo_lex_models_v2.types.test_set_turn_record

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.test_set_turn_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestSetTurnRecordList:
    import capo_lex_models_v2.types.test_set_turn_record

    out: TestSetTurnRecordList = []
    for item in data:
        out.append(capo_lex_models_v2.types.test_set_turn_record.deserialize_json(item))
    return out
