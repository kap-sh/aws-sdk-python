"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Choice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.additional_resources_list
    import aws_sdk_wellarchitected.types.choice_content
    import aws_sdk_wellarchitected.types.choice_description
    import aws_sdk_wellarchitected.types.choice_id
    import aws_sdk_wellarchitected.types.choice_title


class Choice(TypedDict, closed=True):
    choice_id: NotRequired["aws_sdk_wellarchitected.types.choice_id.ChoiceId"]
    title: NotRequired["aws_sdk_wellarchitected.types.choice_title.ChoiceTitle"]
    description: NotRequired[
        "aws_sdk_wellarchitected.types.choice_description.ChoiceDescription"
    ]
    helpful_resource: NotRequired[
        "aws_sdk_wellarchitected.types.choice_content.ChoiceContent"
    ]
    """<p>The helpful resource (both text and URL) for a particular choice.</p> <p>This field only applies to custom lenses. Each choice can have only one helpful resource.</p>"""
    improvement_plan: NotRequired[
        "aws_sdk_wellarchitected.types.choice_content.ChoiceContent"
    ]
    """<p>The improvement plan (both text and URL) for a particular choice.</p> <p>This field only applies to custom lenses. Each choice can have only one improvement plan.</p>"""
    additional_resources: NotRequired[
        "aws_sdk_wellarchitected.types.additional_resources_list.AdditionalResourcesList"
    ]
    """<p>The additional resources for a choice in a custom lens.</p> <p>A choice can have up to two additional resources: one of type <code>HELPFUL_RESOURCE</code>, one of type <code>IMPROVEMENT_PLAN</code>, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Choice) -> dict:
    out: dict = {}
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "helpful_resource" in value:
        import aws_sdk_wellarchitected.types.choice_content

        out["HelpfulResource"] = (
            aws_sdk_wellarchitected.types.choice_content.serialize_json(
                value["helpful_resource"]
            )
        )
    if "improvement_plan" in value:
        import aws_sdk_wellarchitected.types.choice_content

        out["ImprovementPlan"] = (
            aws_sdk_wellarchitected.types.choice_content.serialize_json(
                value["improvement_plan"]
            )
        )
    if "additional_resources" in value:
        import aws_sdk_wellarchitected.types.additional_resources_list

        out["AdditionalResources"] = (
            aws_sdk_wellarchitected.types.additional_resources_list.serialize_json(
                value["additional_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> Choice:
    out: Choice = {}  # type: ignore[typeddict-item]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "HelpfulResource" in data:
        import aws_sdk_wellarchitected.types.choice_content

        out["helpful_resource"] = (
            aws_sdk_wellarchitected.types.choice_content.deserialize_json(
                data["HelpfulResource"]
            )
        )
    if "ImprovementPlan" in data:
        import aws_sdk_wellarchitected.types.choice_content

        out["improvement_plan"] = (
            aws_sdk_wellarchitected.types.choice_content.deserialize_json(
                data["ImprovementPlan"]
            )
        )
    if "AdditionalResources" in data:
        import aws_sdk_wellarchitected.types.additional_resources_list

        out["additional_resources"] = (
            aws_sdk_wellarchitected.types.additional_resources_list.deserialize_json(
                data["AdditionalResources"]
            )
        )
    return out
