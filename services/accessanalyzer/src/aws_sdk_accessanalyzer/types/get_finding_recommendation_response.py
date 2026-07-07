"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.recommendation_error
    import aws_sdk_accessanalyzer.types.recommendation_type
    import aws_sdk_accessanalyzer.types.recommended_step_list
    import aws_sdk_accessanalyzer.types.resource_arn
    import aws_sdk_accessanalyzer.types.status
    import aws_sdk_accessanalyzer.types.timestamp
    import aws_sdk_accessanalyzer.types.token


class GetFindingRecommendationResponse(TypedDict, closed=True):
    started_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the retrieval of the finding recommendation was started.</p>"""
    completed_at: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the retrieval of the finding recommendation was completed.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    error: NotRequired[
        "aws_sdk_accessanalyzer.types.recommendation_error.RecommendationError"
    ]
    """<p>Detailed information about the reason that the retrieval of a recommendation for the finding failed.</p>"""
    resource_arn: "aws_sdk_accessanalyzer.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource of the finding.</p>"""
    recommended_steps: NotRequired[
        "aws_sdk_accessanalyzer.types.recommended_step_list.RecommendedStepList"
    ]
    """<p>A group of recommended steps for the finding.</p>"""
    recommendation_type: (
        "aws_sdk_accessanalyzer.types.recommendation_type.RecommendationType"
    )
    """<p>The type of recommendation for the finding.</p>"""
    status: "aws_sdk_accessanalyzer.types.status.Status"
    """<p>The status of the retrieval of the finding recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingRecommendationResponse) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.timestamp

    out["startedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["started_at"]
    )
    if "completed_at" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["completedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["completed_at"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "error" in value:
        import aws_sdk_accessanalyzer.types.recommendation_error

        out["error"] = aws_sdk_accessanalyzer.types.recommendation_error.serialize_json(
            value["error"]
        )
    out["resourceArn"] = value["resource_arn"]
    if "recommended_steps" in value:
        import aws_sdk_accessanalyzer.types.recommended_step_list

        out["recommendedSteps"] = (
            aws_sdk_accessanalyzer.types.recommended_step_list.serialize_json(
                value["recommended_steps"]
            )
        )
    out["recommendationType"] = value["recommendation_type"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> GetFindingRecommendationResponse:
    out: GetFindingRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "startedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["started_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError(
            "GetFindingRecommendationResponse.started_at required"
        )
    if "completedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["completed_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["completedAt"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "error" in data:
        import aws_sdk_accessanalyzer.types.recommendation_error

        out["error"] = (
            aws_sdk_accessanalyzer.types.recommendation_error.deserialize_json(
                data["error"]
            )
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "GetFindingRecommendationResponse.resource_arn required"
        )
    if "recommendedSteps" in data:
        import aws_sdk_accessanalyzer.types.recommended_step_list

        out["recommended_steps"] = (
            aws_sdk_accessanalyzer.types.recommended_step_list.deserialize_json(
                data["recommendedSteps"]
            )
        )
    if "recommendationType" in data:
        out["recommendation_type"] = data["recommendationType"]
    else:
        raise DeserializationError(
            "GetFindingRecommendationResponse.recommendation_type required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetFindingRecommendationResponse.status required")
    return out
