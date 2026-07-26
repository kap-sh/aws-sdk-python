"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentClassificationTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.intent_classification_test_result_item_list


class IntentClassificationTestResults(TypedDict, closed=True):
    items: "capo_lex_models_v2.types.intent_classification_test_result_item_list.IntentClassificationTestResultItemList"
    """<p>A list of the results for the intent classification test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentClassificationTestResults) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.intent_classification_test_result_item_list

    out["items"] = (
        capo_lex_models_v2.types.intent_classification_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> IntentClassificationTestResults:
    out: IntentClassificationTestResults = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_lex_models_v2.types.intent_classification_test_result_item_list

        out["items"] = (
            capo_lex_models_v2.types.intent_classification_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("IntentClassificationTestResults.items required")
    return out
