"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotRecommendationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_recommendation_status
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.timestamp


class BotRecommendationSummary(TypedDict):
    bot_recommendation_status: (
        "aws_sdk_lex_models_v2.types.bot_recommendation_status.BotRecommendationStatus"
    )
    """<p>The status of the bot recommendation.</p> <p>If the status is Failed, then the reasons for the failure are listed in the failureReasons field. </p>"""
    bot_recommendation_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot recommendation to be updated.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot recommendation was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the date and time that the bot recommendation was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotRecommendationSummary) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.bot_recommendation_status

    out["botRecommendationStatus"] = (
        aws_sdk_lex_models_v2.types.bot_recommendation_status.serialize_json(
            value["bot_recommendation_status"]
        )
    )
    out["botRecommendationId"] = value["bot_recommendation_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BotRecommendationSummary:
    out: BotRecommendationSummary = {}  # type: ignore[typeddict-item]
    if "botRecommendationStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_recommendation_status

        out["bot_recommendation_status"] = (
            aws_sdk_lex_models_v2.types.bot_recommendation_status.deserialize_json(
                data["botRecommendationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "BotRecommendationSummary.bot_recommendation_status required"
        )
    if "botRecommendationId" in data:
        out["bot_recommendation_id"] = data["botRecommendationId"]
    else:
        raise DeserializationError(
            "BotRecommendationSummary.bot_recommendation_id required"
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
