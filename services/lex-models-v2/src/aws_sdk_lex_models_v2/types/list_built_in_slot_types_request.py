"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBuiltInSlotTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_slot_type_sort_by
    import aws_sdk_lex_models_v2.types.built_ins_max_results
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token


class ListBuiltInSlotTypesRequest(TypedDict, closed=True):
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    sort_by: NotRequired[
        "aws_sdk_lex_models_v2.types.built_in_slot_type_sort_by.BuiltInSlotTypeSortBy"
    ]
    """<p>Determines the sort order for the response from the <code>ListBuiltInSlotTypes</code> operation. You can choose to sort by the slot type signature in either ascending or descending order.</p>"""
    max_results: NotRequired[
        "aws_sdk_lex_models_v2.types.built_ins_max_results.BuiltInsMaxResults"
    ]
    """<p>The maximum number of built-in slot types to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListBuiltInSlotTypes</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBuiltInSlotTypesRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_lex_models_v2.types.built_in_slot_type_sort_by

        out["sortBy"] = (
            aws_sdk_lex_models_v2.types.built_in_slot_type_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBuiltInSlotTypesRequest:
    out: ListBuiltInSlotTypesRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import aws_sdk_lex_models_v2.types.built_in_slot_type_sort_by

        out["sort_by"] = (
            aws_sdk_lex_models_v2.types.built_in_slot_type_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
