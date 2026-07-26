"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#PrioritizeBusinessGoals``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.business_goals


class PrioritizeBusinessGoals(TypedDict, closed=True):
    business_goals: NotRequired[
        "capo_migrationhubstrategy.types.business_goals.BusinessGoals"
    ]
    """<p> Rank of business goals based on priority. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrioritizeBusinessGoals) -> dict:
    out: dict = {}
    if "business_goals" in value:
        import capo_migrationhubstrategy.types.business_goals

        out["businessGoals"] = (
            capo_migrationhubstrategy.types.business_goals.serialize_json(
                value["business_goals"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrioritizeBusinessGoals:
    out: PrioritizeBusinessGoals = {}  # type: ignore[typeddict-item]
    if "businessGoals" in data:
        import capo_migrationhubstrategy.types.business_goals

        out["business_goals"] = (
            capo_migrationhubstrategy.types.business_goals.deserialize_json(
                data["businessGoals"]
            )
        )
    return out
