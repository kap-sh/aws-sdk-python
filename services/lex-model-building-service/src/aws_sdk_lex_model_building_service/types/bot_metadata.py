"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BotMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.description
    import aws_sdk_lex_model_building_service.types.status
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.version


class BotMetadata(TypedDict):
    name: NotRequired["aws_sdk_lex_model_building_service.types.bot_name.BotName"]
    """<p>The name of the bot. </p>"""
    description: NotRequired[
        "aws_sdk_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the bot.</p>"""
    status: NotRequired["aws_sdk_lex_model_building_service.types.status.Status"]
    """<p>The status of the bot.</p>"""
    last_updated_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the bot was updated. When you create a bot, the creation date and last updated date are the same. </p>"""
    created_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the bot was created.</p>"""
    version: NotRequired["aws_sdk_lex_model_building_service.types.version.Version"]
    """<p>The version of the bot. For a new bot, the version is always <code>$LATEST</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_lex_model_building_service.types.status

        out["status"] = aws_sdk_lex_model_building_service.types.status.serialize_json(
            value["status"]
        )
    if "last_updated_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> BotMetadata:
    out: BotMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_lex_model_building_service.types.status

        out["status"] = (
            aws_sdk_lex_model_building_service.types.status.deserialize_json(
                data["status"]
            )
        )
    if "lastUpdatedDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "createdDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["created_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
