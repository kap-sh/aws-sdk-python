"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_config
    import capo_customer_profiles.types.recommender_status
    import capo_customer_profiles.types.timestamp


class RecommenderUpdate(TypedDict, closed=True):
    recommender_config: NotRequired[
        "capo_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The updated configuration settings applied to the recommender during this update.</p>"""
    status: NotRequired[
        "capo_customer_profiles.types.recommender_status.RecommenderStatus"
    ]
    """<p>The current status of the recommender update operation.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when this recommender update was initiated.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the recommender was edited.</p>"""
    failure_reason: NotRequired["str"]
    """<p>If the update operation failed, provides the reason for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderUpdate) -> dict:
    out: dict = {}
    if "recommender_config" in value:
        import capo_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            capo_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    if "status" in value:
        import capo_customer_profiles.types.recommender_status

        out["Status"] = capo_customer_profiles.types.recommender_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> RecommenderUpdate:
    out: RecommenderUpdate = {}  # type: ignore[typeddict-item]
    if "RecommenderConfig" in data:
        import capo_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            capo_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    if "Status" in data:
        import capo_customer_profiles.types.recommender_status

        out["status"] = (
            capo_customer_profiles.types.recommender_status.deserialize_json(
                data["Status"]
            )
        )
    if "CreatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
