"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#PutPortfolioPreferencesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.application_mode
    import aws_sdk_migrationhubstrategy.types.application_preferences
    import aws_sdk_migrationhubstrategy.types.database_preferences
    import aws_sdk_migrationhubstrategy.types.prioritize_business_goals


class PutPortfolioPreferencesRequest(TypedDict):
    prioritize_business_goals: NotRequired[
        "aws_sdk_migrationhubstrategy.types.prioritize_business_goals.PrioritizeBusinessGoals"
    ]
    """<p> The rank of the business goals based on priority. </p>"""
    application_preferences: NotRequired[
        "aws_sdk_migrationhubstrategy.types.application_preferences.ApplicationPreferences"
    ]
    """<p> The transformation preferences for non-database applications. </p>"""
    database_preferences: NotRequired[
        "aws_sdk_migrationhubstrategy.types.database_preferences.DatabasePreferences"
    ]
    """<p> The transformation preferences for database applications. </p>"""
    application_mode: NotRequired[
        "aws_sdk_migrationhubstrategy.types.application_mode.ApplicationMode"
    ]
    """<p>The classification for application component types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPortfolioPreferencesRequest) -> dict:
    out: dict = {}
    if "prioritize_business_goals" in value:
        import aws_sdk_migrationhubstrategy.types.prioritize_business_goals

        out["prioritizeBusinessGoals"] = (
            aws_sdk_migrationhubstrategy.types.prioritize_business_goals.serialize_json(
                value["prioritize_business_goals"]
            )
        )
    if "application_preferences" in value:
        import aws_sdk_migrationhubstrategy.types.application_preferences

        out["applicationPreferences"] = (
            aws_sdk_migrationhubstrategy.types.application_preferences.serialize_json(
                value["application_preferences"]
            )
        )
    if "database_preferences" in value:
        import aws_sdk_migrationhubstrategy.types.database_preferences

        out["databasePreferences"] = (
            aws_sdk_migrationhubstrategy.types.database_preferences.serialize_json(
                value["database_preferences"]
            )
        )
    if "application_mode" in value:
        out["applicationMode"] = value["application_mode"]
    return out


def deserialize_json(data: dict) -> PutPortfolioPreferencesRequest:
    out: PutPortfolioPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "prioritizeBusinessGoals" in data:
        import aws_sdk_migrationhubstrategy.types.prioritize_business_goals

        out["prioritize_business_goals"] = (
            aws_sdk_migrationhubstrategy.types.prioritize_business_goals.deserialize_json(
                data["prioritizeBusinessGoals"]
            )
        )
    if "applicationPreferences" in data:
        import aws_sdk_migrationhubstrategy.types.application_preferences

        out["application_preferences"] = (
            aws_sdk_migrationhubstrategy.types.application_preferences.deserialize_json(
                data["applicationPreferences"]
            )
        )
    if "databasePreferences" in data:
        import aws_sdk_migrationhubstrategy.types.database_preferences

        out["database_preferences"] = (
            aws_sdk_migrationhubstrategy.types.database_preferences.deserialize_json(
                data["databasePreferences"]
            )
        )
    if "applicationMode" in data:
        out["application_mode"] = data["applicationMode"]
    return out
