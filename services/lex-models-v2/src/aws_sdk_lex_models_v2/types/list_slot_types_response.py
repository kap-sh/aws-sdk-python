"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListSlotTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.slot_type_summary_list


class ListSlotTypesResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the slot types.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot that contains the slot types.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and local of the slot types in the list.</p>"""
    slot_type_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_type_summary_list.SlotTypeSummaryList"
    ]
    """<p>Summary information for the slot types that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more slot types available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListSlotTypes</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListSlotTypes</code> operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSlotTypesResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "slot_type_summaries" in value:
        import aws_sdk_lex_models_v2.types.slot_type_summary_list

        out["slotTypeSummaries"] = (
            aws_sdk_lex_models_v2.types.slot_type_summary_list.serialize_json(
                value["slot_type_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSlotTypesResponse:
    out: ListSlotTypesResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "slotTypeSummaries" in data:
        import aws_sdk_lex_models_v2.types.slot_type_summary_list

        out["slot_type_summaries"] = (
            aws_sdk_lex_models_v2.types.slot_type_summary_list.deserialize_json(
                data["slotTypeSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
