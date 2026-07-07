"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_status
    import aws_sdk_lex_models_v2.types.bot_version_locale_specification
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.numerical_bot_version
    import aws_sdk_lex_models_v2.types.timestamp


class CreateBotVersionResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The bot identifier specified in the request.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description of the version specified in the request.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The version number assigned to the version.</p>"""
    bot_version_locale_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_version_locale_specification.BotVersionLocaleSpecification"
    ]
    """<p>The source versions used for each locale in the new version.</p>"""
    bot_status: NotRequired["aws_sdk_lex_models_v2.types.bot_status.BotStatus"]
    """<p>When you send a request to create or update a bot, Amazon Lex sets the status response element to <code>Creating</code>. After Amazon Lex builds the bot, it sets status to <code>Available</code>. If Amazon Lex can't build the bot, it sets status to <code>Failed</code>.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotVersionResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_version_locale_specification" in value:
        import aws_sdk_lex_models_v2.types.bot_version_locale_specification

        out["botVersionLocaleSpecification"] = (
            aws_sdk_lex_models_v2.types.bot_version_locale_specification.serialize_json(
                value["bot_version_locale_specification"]
            )
        )
    if "bot_status" in value:
        import aws_sdk_lex_models_v2.types.bot_status

        out["botStatus"] = aws_sdk_lex_models_v2.types.bot_status.serialize_json(
            value["bot_status"]
        )
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateBotVersionResponse:
    out: CreateBotVersionResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "description" in data:
        out["description"] = data["description"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "botVersionLocaleSpecification" in data:
        import aws_sdk_lex_models_v2.types.bot_version_locale_specification

        out["bot_version_locale_specification"] = (
            aws_sdk_lex_models_v2.types.bot_version_locale_specification.deserialize_json(
                data["botVersionLocaleSpecification"]
            )
        )
    if "botStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_status

        out["bot_status"] = aws_sdk_lex_models_v2.types.bot_status.deserialize_json(
            data["botStatus"]
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    return out
