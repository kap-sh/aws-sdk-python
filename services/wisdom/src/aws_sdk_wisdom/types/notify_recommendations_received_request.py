"""Generated from Smithy shape ``com.amazonaws.wisdom#NotifyRecommendationsReceivedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.recommendation_id_list
    import aws_sdk_wisdom.types.uuid_or_arn


class NotifyRecommendationsReceivedRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    session_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    recommendation_ids: (
        "aws_sdk_wisdom.types.recommendation_id_list.RecommendationIdList"
    )
    """<p>The identifiers of the recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotifyRecommendationsReceivedRequest) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.recommendation_id_list

    out["recommendationIds"] = (
        aws_sdk_wisdom.types.recommendation_id_list.serialize_json(
            value["recommendation_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> NotifyRecommendationsReceivedRequest:
    out: NotifyRecommendationsReceivedRequest = {}  # type: ignore[typeddict-item]
    if "recommendationIds" in data:
        import aws_sdk_wisdom.types.recommendation_id_list

        out["recommendation_ids"] = (
            aws_sdk_wisdom.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyRecommendationsReceivedRequest.recommendation_ids required"
        )
    return out
