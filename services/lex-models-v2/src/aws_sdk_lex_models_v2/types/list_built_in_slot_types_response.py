"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBuiltInSlotTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_slot_type_summary_list
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token


class ListBuiltInSlotTypesResponse(TypedDict):
    built_in_slot_type_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.built_in_slot_type_summary_list.BuiltInSlotTypeSummaryList"
    ]
    """<p>Summary information for the built-in slot types that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more slot types available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListBuiltInSlotTypes</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>LIstBuiltInSlotTypes</code> operation request to get the next page of results.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale of the slot types in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBuiltInSlotTypesResponse) -> dict:
    out: dict = {}
    if "built_in_slot_type_summaries" in value:
        import aws_sdk_lex_models_v2.types.built_in_slot_type_summary_list

        out["builtInSlotTypeSummaries"] = (
            aws_sdk_lex_models_v2.types.built_in_slot_type_summary_list.serialize_json(
                value["built_in_slot_type_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> ListBuiltInSlotTypesResponse:
    out: ListBuiltInSlotTypesResponse = {}  # type: ignore[typeddict-item]
    if "builtInSlotTypeSummaries" in data:
        import aws_sdk_lex_models_v2.types.built_in_slot_type_summary_list

        out["built_in_slot_type_summaries"] = (
            aws_sdk_lex_models_v2.types.built_in_slot_type_summary_list.deserialize_json(
                data["builtInSlotTypeSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    return out
