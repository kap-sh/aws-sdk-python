"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StartMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.iam_role_arn
    import aws_sdk_lex_model_building_service.types.migration_strategy
    import aws_sdk_lex_model_building_service.types.v2_bot_name
    import aws_sdk_lex_model_building_service.types.version


class StartMigrationRequest(TypedDict, closed=True):
    v1_bot_name: "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.</p>"""
    v1_bot_version: "aws_sdk_lex_model_building_service.types.version.Version"
    """<p>The version of the bot to migrate to Amazon Lex V2. You can migrate the <code>$LATEST</code> version as well as any numbered version.</p>"""
    v2_bot_name: "aws_sdk_lex_model_building_service.types.v2_bot_name.V2BotName"
    """<p>The name of the Amazon Lex V2 bot that you are migrating the Amazon Lex V1 bot to. </p> <ul> <li> <p>If the Amazon Lex V2 bot doesn't exist, you must use the <code>CREATE_NEW</code> migration strategy.</p> </li> <li> <p>If the Amazon Lex V2 bot exists, you must use the <code>UPDATE_EXISTING</code> migration strategy to change the contents of the Amazon Lex V2 bot.</p> </li> </ul>"""
    v2_bot_role: "aws_sdk_lex_model_building_service.types.iam_role_arn.IamRoleArn"
    """<p>The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.</p>"""
    migration_strategy: (
        "aws_sdk_lex_model_building_service.types.migration_strategy.MigrationStrategy"
    )
    """<p>The strategy used to conduct the migration.</p> <ul> <li> <p> <code>CREATE_NEW</code> - Creates a new Amazon Lex V2 bot and migrates the Amazon Lex V1 bot to the new bot.</p> </li> <li> <p> <code>UPDATE_EXISTING</code> - Overwrites the existing Amazon Lex V2 bot metadata and the locale being migrated. It doesn't change any other locales in the Amazon Lex V2 bot. If the locale doesn't exist, a new locale is created in the Amazon Lex V2 bot.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMigrationRequest) -> dict:
    out: dict = {}
    out["v1BotName"] = value["v1_bot_name"]
    out["v1BotVersion"] = value["v1_bot_version"]
    out["v2BotName"] = value["v2_bot_name"]
    out["v2BotRole"] = value["v2_bot_role"]
    import aws_sdk_lex_model_building_service.types.migration_strategy

    out["migrationStrategy"] = (
        aws_sdk_lex_model_building_service.types.migration_strategy.serialize_json(
            value["migration_strategy"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartMigrationRequest:
    out: StartMigrationRequest = {}  # type: ignore[typeddict-item]
    if "v1BotName" in data:
        out["v1_bot_name"] = data["v1BotName"]
    else:
        raise DeserializationError("StartMigrationRequest.v1_bot_name required")
    if "v1BotVersion" in data:
        out["v1_bot_version"] = data["v1BotVersion"]
    else:
        raise DeserializationError("StartMigrationRequest.v1_bot_version required")
    if "v2BotName" in data:
        out["v2_bot_name"] = data["v2BotName"]
    else:
        raise DeserializationError("StartMigrationRequest.v2_bot_name required")
    if "v2BotRole" in data:
        out["v2_bot_role"] = data["v2BotRole"]
    else:
        raise DeserializationError("StartMigrationRequest.v2_bot_role required")
    if "migrationStrategy" in data:
        import aws_sdk_lex_model_building_service.types.migration_strategy

        out["migration_strategy"] = (
            aws_sdk_lex_model_building_service.types.migration_strategy.deserialize_json(
                data["migrationStrategy"]
            )
        )
    else:
        raise DeserializationError("StartMigrationRequest.migration_strategy required")
    return out
