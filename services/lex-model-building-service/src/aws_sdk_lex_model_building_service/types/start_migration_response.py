"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StartMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.iam_role_arn
    import aws_sdk_lex_model_building_service.types.locale
    import aws_sdk_lex_model_building_service.types.migration_id
    import aws_sdk_lex_model_building_service.types.migration_strategy
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.v2_bot_id
    import aws_sdk_lex_model_building_service.types.version


class StartMigrationResponse(TypedDict, closed=True):
    v1_bot_name: NotRequired[
        "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    ]
    """<p>The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.</p>"""
    v1_bot_version: NotRequired[
        "aws_sdk_lex_model_building_service.types.version.Version"
    ]
    """<p>The version of the bot to migrate to Amazon Lex V2. </p>"""
    v1_bot_locale: NotRequired["aws_sdk_lex_model_building_service.types.locale.Locale"]
    """<p>The locale used for the Amazon Lex V1 bot. </p>"""
    v2_bot_id: NotRequired["aws_sdk_lex_model_building_service.types.v2_bot_id.V2BotId"]
    """<p>The unique identifier for the Amazon Lex V2 bot. </p>"""
    v2_bot_role: NotRequired[
        "aws_sdk_lex_model_building_service.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.</p>"""
    migration_id: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_id.MigrationId"
    ]
    """<p>The unique identifier that Amazon Lex assigned to the migration.</p>"""
    migration_strategy: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_strategy.MigrationStrategy"
    ]
    """<p>The strategy used to conduct the migration.</p>"""
    migration_timestamp: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the migration started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMigrationResponse) -> dict:
    out: dict = {}
    if "v1_bot_name" in value:
        out["v1BotName"] = value["v1_bot_name"]
    if "v1_bot_version" in value:
        out["v1BotVersion"] = value["v1_bot_version"]
    if "v1_bot_locale" in value:
        import aws_sdk_lex_model_building_service.types.locale

        out["v1BotLocale"] = (
            aws_sdk_lex_model_building_service.types.locale.serialize_json(
                value["v1_bot_locale"]
            )
        )
    if "v2_bot_id" in value:
        out["v2BotId"] = value["v2_bot_id"]
    if "v2_bot_role" in value:
        out["v2BotRole"] = value["v2_bot_role"]
    if "migration_id" in value:
        out["migrationId"] = value["migration_id"]
    if "migration_strategy" in value:
        import aws_sdk_lex_model_building_service.types.migration_strategy

        out["migrationStrategy"] = (
            aws_sdk_lex_model_building_service.types.migration_strategy.serialize_json(
                value["migration_strategy"]
            )
        )
    if "migration_timestamp" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["migrationTimestamp"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["migration_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartMigrationResponse:
    out: StartMigrationResponse = {}  # type: ignore[typeddict-item]
    if "v1BotName" in data:
        out["v1_bot_name"] = data["v1BotName"]
    if "v1BotVersion" in data:
        out["v1_bot_version"] = data["v1BotVersion"]
    if "v1BotLocale" in data:
        import aws_sdk_lex_model_building_service.types.locale

        out["v1_bot_locale"] = (
            aws_sdk_lex_model_building_service.types.locale.deserialize_json(
                data["v1BotLocale"]
            )
        )
    if "v2BotId" in data:
        out["v2_bot_id"] = data["v2BotId"]
    if "v2BotRole" in data:
        out["v2_bot_role"] = data["v2BotRole"]
    if "migrationId" in data:
        out["migration_id"] = data["migrationId"]
    if "migrationStrategy" in data:
        import aws_sdk_lex_model_building_service.types.migration_strategy

        out["migration_strategy"] = (
            aws_sdk_lex_model_building_service.types.migration_strategy.deserialize_json(
                data["migrationStrategy"]
            )
        )
    if "migrationTimestamp" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["migration_timestamp"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["migrationTimestamp"]
            )
        )
    return out
