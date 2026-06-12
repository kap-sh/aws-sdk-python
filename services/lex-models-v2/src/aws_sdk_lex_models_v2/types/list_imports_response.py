"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListImportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.import_summary_list
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token


class ListImportsResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier assigned by Amazon Lex to the bot.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that was imported. It will always be <code>DRAFT</code>.</p>"""
    import_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.import_summary_list.ImportSummaryList"
    ]
    """<p>Summary information for the imports that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter. If there are more imports available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListImports</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListImports</code> operation request to get the next page of results.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale specified in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "import_summaries" in value:
        import aws_sdk_lex_models_v2.types.import_summary_list

        out["importSummaries"] = (
            aws_sdk_lex_models_v2.types.import_summary_list.serialize_json(
                value["import_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> ListImportsResponse:
    out: ListImportsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "importSummaries" in data:
        import aws_sdk_lex_models_v2.types.import_summary_list

        out["import_summaries"] = (
            aws_sdk_lex_models_v2.types.import_summary_list.deserialize_json(
                data["importSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    return out
