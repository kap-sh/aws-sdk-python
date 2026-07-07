"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.iam_role_arn
    import aws_sdk_lex_model_building_service.types.locale
    import aws_sdk_lex_model_building_service.types.migration_alerts
    import aws_sdk_lex_model_building_service.types.migration_id
    import aws_sdk_lex_model_building_service.types.migration_status
    import aws_sdk_lex_model_building_service.types.migration_strategy
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.v2_bot_id
    import aws_sdk_lex_model_building_service.types.version


class GetMigrationResponse(TypedDict, closed=True):
    migration_id: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_id.MigrationId"
    ]
    """<p>The unique identifier of the migration. This is the same as the identifier used when calling the <code>GetMigration</code> operation.</p>"""
    v1_bot_name: NotRequired[
        "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    ]
    """<p>The name of the Amazon Lex V1 bot migrated to Amazon Lex V2.</p>"""
    v1_bot_version: NotRequired[
        "aws_sdk_lex_model_building_service.types.version.Version"
    ]
    """<p>The version of the Amazon Lex V1 bot migrated to Amazon Lex V2.</p>"""
    v1_bot_locale: NotRequired["aws_sdk_lex_model_building_service.types.locale.Locale"]
    """<p>The locale of the Amazon Lex V1 bot migrated to Amazon Lex V2.</p>"""
    v2_bot_id: NotRequired["aws_sdk_lex_model_building_service.types.v2_bot_id.V2BotId"]
    """<p>The unique identifier of the Amazon Lex V2 bot that the Amazon Lex V1 is being migrated to.</p>"""
    v2_bot_role: NotRequired[
        "aws_sdk_lex_model_building_service.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.</p>"""
    migration_status: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_status.MigrationStatus"
    ]
    """<p>Indicates the status of the migration. When the status is <code>COMPLETE</code> the migration is finished and the bot is available in Amazon Lex V2. There may be alerts and warnings that need to be resolved to complete the migration.</p>"""
    migration_strategy: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_strategy.MigrationStrategy"
    ]
    """<p>The strategy used to conduct the migration.</p> <ul> <li> <p> <code>CREATE_NEW</code> - Creates a new Amazon Lex V2 bot and migrates the Amazon Lex V1 bot to the new bot.</p> </li> <li> <p> <code>UPDATE_EXISTING</code> - Overwrites the existing Amazon Lex V2 bot metadata and the locale being migrated. It doesn't change any other locales in the Amazon Lex V2 bot. If the locale doesn't exist, a new locale is created in the Amazon Lex V2 bot.</p> </li> </ul>"""
    migration_timestamp: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the migration started.</p>"""
    alerts: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_alerts.MigrationAlerts"
    ]
    r"""<p>A list of alerts and warnings that indicate issues with the migration for the Amazon Lex V1 bot to Amazon Lex V2. You receive a warning when an Amazon Lex V1 feature has a different implementation if Amazon Lex V2.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/migrate.html\">Migrating a bot</a> in the <i>Amazon Lex V2 developer guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationResponse) -> dict:
    out: dict = {}
    if "migration_id" in value:
        out["migrationId"] = value["migration_id"]
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
    if "migration_status" in value:
        import aws_sdk_lex_model_building_service.types.migration_status

        out["migrationStatus"] = (
            aws_sdk_lex_model_building_service.types.migration_status.serialize_json(
                value["migration_status"]
            )
        )
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
    if "alerts" in value:
        import aws_sdk_lex_model_building_service.types.migration_alerts

        out["alerts"] = (
            aws_sdk_lex_model_building_service.types.migration_alerts.serialize_json(
                value["alerts"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMigrationResponse:
    out: GetMigrationResponse = {}  # type: ignore[typeddict-item]
    if "migrationId" in data:
        out["migration_id"] = data["migrationId"]
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
    if "migrationStatus" in data:
        import aws_sdk_lex_model_building_service.types.migration_status

        out["migration_status"] = (
            aws_sdk_lex_model_building_service.types.migration_status.deserialize_json(
                data["migrationStatus"]
            )
        )
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
    if "alerts" in data:
        import aws_sdk_lex_model_building_service.types.migration_alerts

        out["alerts"] = (
            aws_sdk_lex_model_building_service.types.migration_alerts.deserialize_json(
                data["alerts"]
            )
        )
    return out
