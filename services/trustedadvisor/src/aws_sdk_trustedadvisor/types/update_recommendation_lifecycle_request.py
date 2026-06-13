"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationLifecycleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.account_recommendation_identifier
    import aws_sdk_trustedadvisor.types.recommendation_update_reason
    import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage
    import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code


class UpdateRecommendationLifecycleRequest(TypedDict):
    lifecycle_stage: "aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage.UpdateRecommendationLifecycleStage"
    """<p>The new lifecycle stage</p>"""
    update_reason: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_update_reason.RecommendationUpdateReason"
    ]
    """<p>Reason for the lifecycle stage change</p>"""
    update_reason_code: NotRequired[
        "aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.UpdateRecommendationLifecycleStageReasonCode"
    ]
    """<p>Reason code for the lifecycle state change</p>"""
    recommendation_identifier: "aws_sdk_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier"
    """<p>The Recommendation identifier for AWS Trusted Advisor Priority recommendations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationLifecycleRequest) -> dict:
    out: dict = {}
    import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage

    out["lifecycleStage"] = (
        aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage.serialize_json(
            value["lifecycle_stage"]
        )
    )
    if "update_reason" in value:
        out["updateReason"] = value["update_reason"]
    if "update_reason_code" in value:
        import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code

        out["updateReasonCode"] = (
            aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.serialize_json(
                value["update_reason_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecommendationLifecycleRequest:
    out: UpdateRecommendationLifecycleRequest = {}  # type: ignore[typeddict-item]
    if "lifecycleStage" in data:
        import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage

        out["lifecycle_stage"] = (
            aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage.deserialize_json(
                data["lifecycleStage"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRecommendationLifecycleRequest.lifecycle_stage required"
        )
    if "updateReason" in data:
        out["update_reason"] = data["updateReason"]
    if "updateReasonCode" in data:
        import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code

        out["update_reason_code"] = (
            aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.deserialize_json(
                data["updateReasonCode"]
            )
        )
    return out
