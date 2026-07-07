"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemUserJourneyUpdatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.user_journey_changes


class SystemUserJourneyUpdatedMetadata(TypedDict, closed=True):
    user_journey_name: NotRequired["str"]
    """<p>The name of the updated user journey.</p>"""
    changes: NotRequired[
        "aws_sdk_resiliencehubv2.types.user_journey_changes.UserJourneyChanges"
    ]
    """<p>The changes made to the user journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemUserJourneyUpdatedMetadata) -> dict:
    out: dict = {}
    if "user_journey_name" in value:
        out["userJourneyName"] = value["user_journey_name"]
    if "changes" in value:
        import aws_sdk_resiliencehubv2.types.user_journey_changes

        out["changes"] = (
            aws_sdk_resiliencehubv2.types.user_journey_changes.serialize_json(
                value["changes"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemUserJourneyUpdatedMetadata:
    out: SystemUserJourneyUpdatedMetadata = {}  # type: ignore[typeddict-item]
    if "userJourneyName" in data:
        out["user_journey_name"] = data["userJourneyName"]
    if "changes" in data:
        import aws_sdk_resiliencehubv2.types.user_journey_changes

        out["changes"] = (
            aws_sdk_resiliencehubv2.types.user_journey_changes.deserialize_json(
                data["changes"]
            )
        )
    return out
