"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.management_preference


class ApplicationPreferences(TypedDict, closed=True):
    management_preference: NotRequired[
        "aws_sdk_migrationhubstrategy.types.management_preference.ManagementPreference"
    ]
    """<p> Application preferences that you specify to prefer managed environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPreferences) -> dict:
    out: dict = {}
    if "management_preference" in value:
        import aws_sdk_migrationhubstrategy.types.management_preference

        out["managementPreference"] = (
            aws_sdk_migrationhubstrategy.types.management_preference.serialize_json(
                value["management_preference"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationPreferences:
    out: ApplicationPreferences = {}  # type: ignore[typeddict-item]
    if "managementPreference" in data:
        import aws_sdk_migrationhubstrategy.types.management_preference

        out["management_preference"] = (
            aws_sdk_migrationhubstrategy.types.management_preference.deserialize_json(
                data["managementPreference"]
            )
        )
    return out
