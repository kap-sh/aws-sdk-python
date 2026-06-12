"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SearchAssociatedTranscriptsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.associated_transcript_list
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_index


class SearchAssociatedTranscriptsResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot associated with the transcripts that you are searching.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot containing the transcripts that you are searching.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> </p>"""
    bot_recommendation_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p> The unique identifier of the bot recommendation associated with the transcripts to search.</p>"""
    next_index: NotRequired["aws_sdk_lex_models_v2.types.next_index.NextIndex"]
    """<p>A index that indicates whether there are more results to return in a response to the SearchAssociatedTranscripts operation. If the nextIndex field is present, you send the contents as the nextIndex parameter of a SearchAssociatedTranscriptsRequest operation to get the next page of results.</p>"""
    associated_transcripts: NotRequired[
        "aws_sdk_lex_models_v2.types.associated_transcript_list.AssociatedTranscriptList"
    ]
    """<p>The object that contains the associated transcript that meet the criteria you specified.</p>"""
    total_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The total number of transcripts returned by the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAssociatedTranscriptsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_recommendation_id" in value:
        out["botRecommendationId"] = value["bot_recommendation_id"]
    if "next_index" in value:
        out["nextIndex"] = value["next_index"]
    if "associated_transcripts" in value:
        import aws_sdk_lex_models_v2.types.associated_transcript_list

        out["associatedTranscripts"] = (
            aws_sdk_lex_models_v2.types.associated_transcript_list.serialize_json(
                value["associated_transcripts"]
            )
        )
    if "total_results" in value:
        out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchAssociatedTranscriptsResponse:
    out: SearchAssociatedTranscriptsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botRecommendationId" in data:
        out["bot_recommendation_id"] = data["botRecommendationId"]
    if "nextIndex" in data:
        out["next_index"] = data["nextIndex"]
    if "associatedTranscripts" in data:
        import aws_sdk_lex_models_v2.types.associated_transcript_list

        out["associated_transcripts"] = (
            aws_sdk_lex_models_v2.types.associated_transcript_list.deserialize_json(
                data["associatedTranscripts"]
            )
        )
    if "totalResults" in data:
        out["total_results"] = data["totalResults"]
    return out
