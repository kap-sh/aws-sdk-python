"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileTemplateChoice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice_description
    import aws_sdk_wellarchitected.types.choice_id
    import aws_sdk_wellarchitected.types.choice_title


class ProfileTemplateChoice(TypedDict):
    choice_id: NotRequired["aws_sdk_wellarchitected.types.choice_id.ChoiceId"]
    choice_title: NotRequired["aws_sdk_wellarchitected.types.choice_title.ChoiceTitle"]
    choice_description: NotRequired[
        "aws_sdk_wellarchitected.types.choice_description.ChoiceDescription"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTemplateChoice) -> dict:
    out: dict = {}
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "choice_title" in value:
        out["ChoiceTitle"] = value["choice_title"]
    if "choice_description" in value:
        out["ChoiceDescription"] = value["choice_description"]
    return out


def deserialize_json(data: dict) -> ProfileTemplateChoice:
    out: ProfileTemplateChoice = {}  # type: ignore[typeddict-item]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    if "ChoiceTitle" in data:
        out["choice_title"] = data["ChoiceTitle"]
    if "ChoiceDescription" in data:
        out["choice_description"] = data["ChoiceDescription"]
    return out
