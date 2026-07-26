"""Generated from Smithy shape ``com.amazonaws.wellarchitected#BestPractice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.choice_title


class BestPractice(TypedDict, closed=True):
    choice_id: NotRequired["capo_wellarchitected.types.choice_id.ChoiceId"]
    choice_title: NotRequired["capo_wellarchitected.types.choice_title.ChoiceTitle"]


# --- restJson1 ser/de ---
def serialize_json(value: BestPractice) -> dict:
    out: dict = {}
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "choice_title" in value:
        out["ChoiceTitle"] = value["choice_title"]
    return out


def deserialize_json(data: dict) -> BestPractice:
    out: BestPractice = {}  # type: ignore[typeddict-item]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    if "ChoiceTitle" in data:
        out["choice_title"] = data["ChoiceTitle"]
    return out
