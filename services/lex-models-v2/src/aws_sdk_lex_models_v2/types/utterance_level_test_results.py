"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceLevelTestResults``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.utterance_level_test_result_item_list


class UtteranceLevelTestResults(TypedDict):
    items: "aws_sdk_lex_models_v2.types.utterance_level_test_result_item_list.UtteranceLevelTestResultItemList"
    """<p>Contains information about an utterance in the results of the test set execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceLevelTestResults) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.utterance_level_test_result_item_list

    out["items"] = (
        aws_sdk_lex_models_v2.types.utterance_level_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> UtteranceLevelTestResults:
    out: UtteranceLevelTestResults = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_lex_models_v2.types.utterance_level_test_result_item_list

        out["items"] = (
            aws_sdk_lex_models_v2.types.utterance_level_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("UtteranceLevelTestResults.items required")
    return out
