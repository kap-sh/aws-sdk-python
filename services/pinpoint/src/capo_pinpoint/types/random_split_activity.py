"""Generated from Smithy shape ``com.amazonaws.pinpoint#RandomSplitActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.list_of_random_split_entry


class RandomSplitActivity(TypedDict, closed=True):
    branches: NotRequired[
        "capo_pinpoint.types.list_of_random_split_entry.ListOfRandomSplitEntry"
    ]
    """<p>The paths for the activity, including the percentage of participants to enter each path and the activity to perform for each path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RandomSplitActivity) -> dict:
    out: dict = {}
    if "branches" in value:
        import capo_pinpoint.types.list_of_random_split_entry

        out["Branches"] = capo_pinpoint.types.list_of_random_split_entry.serialize_json(
            value["branches"]
        )
    return out


def deserialize_json(data: dict) -> RandomSplitActivity:
    out: RandomSplitActivity = {}  # type: ignore[typeddict-item]
    if "Branches" in data:
        import capo_pinpoint.types.list_of_random_split_entry

        out["branches"] = (
            capo_pinpoint.types.list_of_random_split_entry.deserialize_json(
                data["Branches"]
            )
        )
    return out
