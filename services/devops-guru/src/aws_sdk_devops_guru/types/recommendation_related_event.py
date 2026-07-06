"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.recommendation_related_event_name
    import aws_sdk_devops_guru.types.recommendation_related_event_resources


class RecommendationRelatedEvent(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_devops_guru.types.recommendation_related_event_name.RecommendationRelatedEventName"
    ]
    """<p> The name of the event. This corresponds to the <code>Name</code> field in an <code>Event</code> object. </p>"""
    resources: NotRequired[
        "aws_sdk_devops_guru.types.recommendation_related_event_resources.RecommendationRelatedEventResources"
    ]
    """<p> A <code>ResourceCollection</code> object that contains arrays of the names of Amazon Web Services CloudFormation stacks. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedEvent) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "resources" in value:
        import aws_sdk_devops_guru.types.recommendation_related_event_resources

        out["Resources"] = (
            aws_sdk_devops_guru.types.recommendation_related_event_resources.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommendationRelatedEvent:
    out: RecommendationRelatedEvent = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Resources" in data:
        import aws_sdk_devops_guru.types.recommendation_related_event_resources

        out["resources"] = (
            aws_sdk_devops_guru.types.recommendation_related_event_resources.deserialize_json(
                data["Resources"]
            )
        )
    return out
