"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetPortfolioPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_mode
    import capo_migrationhubstrategy.types.application_preferences
    import capo_migrationhubstrategy.types.database_preferences
    import capo_migrationhubstrategy.types.prioritize_business_goals


class GetPortfolioPreferencesResponse(TypedDict, closed=True):
    prioritize_business_goals: NotRequired[
        "capo_migrationhubstrategy.types.prioritize_business_goals.PrioritizeBusinessGoals"
    ]
    """<p> The rank of business goals based on priority. </p>"""
    application_preferences: NotRequired[
        "capo_migrationhubstrategy.types.application_preferences.ApplicationPreferences"
    ]
    """<p> The transformation preferences for non-database applications. </p>"""
    database_preferences: NotRequired[
        "capo_migrationhubstrategy.types.database_preferences.DatabasePreferences"
    ]
    """<p> The transformation preferences for database applications. </p>"""
    application_mode: NotRequired[
        "capo_migrationhubstrategy.types.application_mode.ApplicationMode"
    ]
    """<p>The classification for application component types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortfolioPreferencesResponse) -> dict:
    out: dict = {}
    if "prioritize_business_goals" in value:
        import capo_migrationhubstrategy.types.prioritize_business_goals

        out["prioritizeBusinessGoals"] = (
            capo_migrationhubstrategy.types.prioritize_business_goals.serialize_json(
                value["prioritize_business_goals"]
            )
        )
    if "application_preferences" in value:
        import capo_migrationhubstrategy.types.application_preferences

        out["applicationPreferences"] = (
            capo_migrationhubstrategy.types.application_preferences.serialize_json(
                value["application_preferences"]
            )
        )
    if "database_preferences" in value:
        import capo_migrationhubstrategy.types.database_preferences

        out["databasePreferences"] = (
            capo_migrationhubstrategy.types.database_preferences.serialize_json(
                value["database_preferences"]
            )
        )
    if "application_mode" in value:
        out["applicationMode"] = value["application_mode"]
    return out


def deserialize_json(data: dict) -> GetPortfolioPreferencesResponse:
    out: GetPortfolioPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "prioritizeBusinessGoals" in data:
        import capo_migrationhubstrategy.types.prioritize_business_goals

        out["prioritize_business_goals"] = (
            capo_migrationhubstrategy.types.prioritize_business_goals.deserialize_json(
                data["prioritizeBusinessGoals"]
            )
        )
    if "applicationPreferences" in data:
        import capo_migrationhubstrategy.types.application_preferences

        out["application_preferences"] = (
            capo_migrationhubstrategy.types.application_preferences.deserialize_json(
                data["applicationPreferences"]
            )
        )
    if "databasePreferences" in data:
        import capo_migrationhubstrategy.types.database_preferences

        out["database_preferences"] = (
            capo_migrationhubstrategy.types.database_preferences.deserialize_json(
                data["databasePreferences"]
            )
        )
    if "applicationMode" in data:
        out["application_mode"] = data["applicationMode"]
    return out
