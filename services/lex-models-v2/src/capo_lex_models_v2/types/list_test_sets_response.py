"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListTestSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.test_set_summary_list


class ListTestSetsResponse(TypedDict, closed=True):
    test_sets: NotRequired[
        "capo_lex_models_v2.types.test_set_summary_list.TestSetSummaryList"
    ]
    """<p>The selected test sets in a list of test sets.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the ListTestSets operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListTestSets operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestSetsResponse) -> dict:
    out: dict = {}
    if "test_sets" in value:
        import capo_lex_models_v2.types.test_set_summary_list

        out["testSets"] = capo_lex_models_v2.types.test_set_summary_list.serialize_json(
            value["test_sets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestSetsResponse:
    out: ListTestSetsResponse = {}  # type: ignore[typeddict-item]
    if "testSets" in data:
        import capo_lex_models_v2.types.test_set_summary_list

        out["test_sets"] = (
            capo_lex_models_v2.types.test_set_summary_list.deserialize_json(
                data["testSets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
