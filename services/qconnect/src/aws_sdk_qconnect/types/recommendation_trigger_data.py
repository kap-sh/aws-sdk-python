"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationTriggerData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.query_recommendation_trigger_data


class _RecommendationTriggerData_query(TypedDict, closed=True):
    query: "aws_sdk_qconnect.types.query_recommendation_trigger_data.QueryRecommendationTriggerData"


RecommendationTriggerData: TypeAlias = _RecommendationTriggerData_query


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTriggerData) -> dict:
    if "query" in value:
        import aws_sdk_qconnect.types.query_recommendation_trigger_data

        return {
            "query": aws_sdk_qconnect.types.query_recommendation_trigger_data.serialize_json(
                value["query"]
            )
        }
    else:
        raise SerializationError("RecommendationTriggerData: no variant present")


def deserialize_json(data: dict) -> RecommendationTriggerData:
    if "query" in data:
        import aws_sdk_qconnect.types.query_recommendation_trigger_data

        return {
            "query": aws_sdk_qconnect.types.query_recommendation_trigger_data.deserialize_json(
                data["query"]
            )
        }
    else:
        raise DeserializationError(
            "RecommendationTriggerData: no recognized variant key"
        )
