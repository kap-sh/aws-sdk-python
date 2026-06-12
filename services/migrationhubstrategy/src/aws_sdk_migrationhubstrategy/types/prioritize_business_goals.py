"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#PrioritizeBusinessGoals``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.business_goals


class PrioritizeBusinessGoals(TypedDict):
    business_goals: NotRequired[
        "aws_sdk_migrationhubstrategy.types.business_goals.BusinessGoals"
    ]
    """<p> Rank of business goals based on priority. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrioritizeBusinessGoals) -> dict:
    out: dict = {}
    if "business_goals" in value:
        import aws_sdk_migrationhubstrategy.types.business_goals

        out["businessGoals"] = (
            aws_sdk_migrationhubstrategy.types.business_goals.serialize_json(
                value["business_goals"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrioritizeBusinessGoals:
    out: PrioritizeBusinessGoals = {}  # type: ignore[typeddict-item]
    if "businessGoals" in data:
        import aws_sdk_migrationhubstrategy.types.business_goals

        out["business_goals"] = (
            aws_sdk_migrationhubstrategy.types.business_goals.deserialize_json(
                data["businessGoals"]
            )
        )
    return out
