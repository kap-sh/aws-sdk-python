"""Generated from Smithy shape ``com.amazonaws.wisdom#RecommendationTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.recommendation_id_list
    import aws_sdk_wisdom.types.recommendation_source_type
    import aws_sdk_wisdom.types.recommendation_trigger_data
    import aws_sdk_wisdom.types.recommendation_trigger_type
    import aws_sdk_wisdom.types.uuid


class RecommendationTrigger(TypedDict, closed=True):
    id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the recommendation trigger.</p>"""
    type: "aws_sdk_wisdom.types.recommendation_trigger_type.RecommendationTriggerType"
    """<p>The type of recommendation trigger.</p>"""
    source: "aws_sdk_wisdom.types.recommendation_source_type.RecommendationSourceType"
    """<p>The source of the recommendation trigger.</p> <ul> <li> <p>ISSUE_DETECTION: The corresponding recommendations were triggered by a Contact Lens issue.</p> </li> <li> <p>RULE_EVALUATION: The corresponding recommendations were triggered by a Contact Lens rule.</p> </li> </ul>"""
    data: "aws_sdk_wisdom.types.recommendation_trigger_data.RecommendationTriggerData"
    """<p>A union type containing information related to the trigger.</p>"""
    recommendation_ids: (
        "aws_sdk_wisdom.types.recommendation_id_list.RecommendationIdList"
    )
    """<p>The identifiers of the recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTrigger) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["source"] = value["source"]
    import aws_sdk_wisdom.types.recommendation_trigger_data

    out["data"] = aws_sdk_wisdom.types.recommendation_trigger_data.serialize_json(
        value["data"]
    )
    import aws_sdk_wisdom.types.recommendation_id_list

    out["recommendationIds"] = (
        aws_sdk_wisdom.types.recommendation_id_list.serialize_json(
            value["recommendation_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> RecommendationTrigger:
    out: RecommendationTrigger = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RecommendationTrigger.id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("RecommendationTrigger.type required")
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("RecommendationTrigger.source required")
    if "data" in data:
        import aws_sdk_wisdom.types.recommendation_trigger_data

        out["data"] = aws_sdk_wisdom.types.recommendation_trigger_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("RecommendationTrigger.data required")
    if "recommendationIds" in data:
        import aws_sdk_wisdom.types.recommendation_id_list

        out["recommendation_ids"] = (
            aws_sdk_wisdom.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    else:
        raise DeserializationError("RecommendationTrigger.recommendation_ids required")
    return out
