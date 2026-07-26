"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_filter_expression
    import capo_customer_profiles.types.recommender_filter_name
    import capo_customer_profiles.types.recommender_filter_status
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class GetRecommenderFilterResponse(TypedDict, closed=True):
    recommender_filter_name: (
        "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName"
    )
    """<p>The name of the recommender filter.</p>"""
    recommender_filter_expression: "capo_customer_profiles.types.recommender_filter_expression.RecommenderFilterExpression"
    """<p>The filter expression that defines which items to include or exclude from recommendations.</p>"""
    recommender_schema_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema associated with this recommender filter.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the recommender filter was created.</p>"""
    status: (
        "capo_customer_profiles.types.recommender_filter_status.RecommenderFilterStatus"
    )
    """<p>The status of the recommender filter.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the recommender filter.</p>"""
    failure_reason: NotRequired["str"]
    """<p>If the recommender filter failed, provides the reason for the failure.</p>"""
    tags: "capo_customer_profiles.types.tag_map.TagMap"
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderFilterResponse) -> dict:
    out: dict = {}
    out["RecommenderFilterName"] = value["recommender_filter_name"]
    out["RecommenderFilterExpression"] = value["recommender_filter_expression"]
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.recommender_filter_status

    out["Status"] = (
        capo_customer_profiles.types.recommender_filter_status.serialize_json(
            value["status"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    import capo_customer_profiles.types.tag_map

    out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetRecommenderFilterResponse:
    out: GetRecommenderFilterResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderFilterName" in data:
        out["recommender_filter_name"] = data["RecommenderFilterName"]
    else:
        raise DeserializationError(
            "GetRecommenderFilterResponse.recommender_filter_name required"
        )
    if "RecommenderFilterExpression" in data:
        out["recommender_filter_expression"] = data["RecommenderFilterExpression"]
    else:
        raise DeserializationError(
            "GetRecommenderFilterResponse.recommender_filter_expression required"
        )
    if "RecommenderSchemaName" in data:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if "CreatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("GetRecommenderFilterResponse.created_at required")
    if "Status" in data:
        import capo_customer_profiles.types.recommender_filter_status

        out["status"] = (
            capo_customer_profiles.types.recommender_filter_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("GetRecommenderFilterResponse.status required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Tags" in data:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("GetRecommenderFilterResponse.tags required")
    return out
