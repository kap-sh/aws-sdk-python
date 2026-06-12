"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OverallTestResults``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.overall_test_result_item_list


class OverallTestResults(TypedDict):
    items: "aws_sdk_lex_models_v2.types.overall_test_result_item_list.OverallTestResultItemList"
    """<p>A list of the overall test results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverallTestResults) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.overall_test_result_item_list

    out["items"] = (
        aws_sdk_lex_models_v2.types.overall_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> OverallTestResults:
    out: OverallTestResults = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_lex_models_v2.types.overall_test_result_item_list

        out["items"] = (
            aws_sdk_lex_models_v2.types.overall_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("OverallTestResults.items required")
    return out
