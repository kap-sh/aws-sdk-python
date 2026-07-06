"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListExportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.export_summary_list
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token


class ListExportsResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier assigned to the bot by Amazon Lex.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot that was exported.</p>"""
    export_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.export_summary_list.ExportSummaryList"
    ]
    """<p>Summary information for the exports that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter. If there are more exports available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListExports</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListExports</code> operation request to get the next page of results.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale specified in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "export_summaries" in value:
        import aws_sdk_lex_models_v2.types.export_summary_list

        out["exportSummaries"] = (
            aws_sdk_lex_models_v2.types.export_summary_list.serialize_json(
                value["export_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> ListExportsResponse:
    out: ListExportsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "exportSummaries" in data:
        import aws_sdk_lex_models_v2.types.export_summary_list

        out["export_summaries"] = (
            aws_sdk_lex_models_v2.types.export_summary_list.deserialize_json(
                data["exportSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    return out
