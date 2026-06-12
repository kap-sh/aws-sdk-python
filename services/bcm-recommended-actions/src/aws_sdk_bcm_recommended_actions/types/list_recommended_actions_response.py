"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ListRecommendedActionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_recommended_actions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_recommended_actions.types.next_token
    import aws_sdk_bcm_recommended_actions.types.recommended_actions


class ListRecommendedActionsResponse(TypedDict):
    recommended_actions: (
        "aws_sdk_bcm_recommended_actions.types.recommended_actions.RecommendedActions"
    )
    """<p>The list of recommended actions that satisfy the filter criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_recommended_actions.types.next_token.NextToken"
    ]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bcm_recommended_actions.types.recommended_actions

    out["recommendedActions"] = (
        aws_sdk_bcm_recommended_actions.types.recommended_actions.serialize_aws_json_1_0(
            value["recommended_actions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendedActionsResponse:
    out: ListRecommendedActionsResponse = {}  # type: ignore[typeddict-item]
    if "recommendedActions" in data:
        import aws_sdk_bcm_recommended_actions.types.recommended_actions

        out["recommended_actions"] = (
            aws_sdk_bcm_recommended_actions.types.recommended_actions.deserialize_aws_json_1_0(
                data["recommendedActions"]
            )
        )
    else:
        raise DeserializationError(
            "ListRecommendedActionsResponse.recommended_actions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
