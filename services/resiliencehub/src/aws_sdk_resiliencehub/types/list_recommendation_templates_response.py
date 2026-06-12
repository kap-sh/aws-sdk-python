"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListRecommendationTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.next_token
    import aws_sdk_resiliencehub.types.recommendation_template_list


class ListRecommendationTemplatesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""
    recommendation_templates: NotRequired[
        "aws_sdk_resiliencehub.types.recommendation_template_list.RecommendationTemplateList"
    ]
    """<p>The recommendation templates for the Resilience Hub applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationTemplatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_templates" in value:
        import aws_sdk_resiliencehub.types.recommendation_template_list

        out["recommendationTemplates"] = (
            aws_sdk_resiliencehub.types.recommendation_template_list.serialize_json(
                value["recommendation_templates"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommendationTemplatesResponse:
    out: ListRecommendationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "recommendationTemplates" in data:
        import aws_sdk_resiliencehub.types.recommendation_template_list

        out["recommendation_templates"] = (
            aws_sdk_resiliencehub.types.recommendation_template_list.deserialize_json(
                data["recommendationTemplates"]
            )
        )
    return out
