"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_config
    import aws_sdk_customer_profiles.types.recommender_status
    import aws_sdk_customer_profiles.types.timestamp


class RecommenderUpdate(TypedDict):
    recommender_config: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The updated configuration settings applied to the recommender during this update.</p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_status.RecommenderStatus"
    ]
    """<p>The current status of the recommender update operation.</p>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when this recommender update was initiated.</p>"""
    last_updated_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the recommender was edited.</p>"""
    failure_reason: NotRequired["str"]
    """<p>If the update operation failed, provides the reason for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderUpdate) -> dict:
    out: dict = {}
    if "recommender_config" in value:
        import aws_sdk_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            aws_sdk_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    if "status" in value:
        import aws_sdk_customer_profiles.types.recommender_status

        out["Status"] = (
            aws_sdk_customer_profiles.types.recommender_status.serialize_json(
                value["status"]
            )
        )
    if "created_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> RecommenderUpdate:
    out: RecommenderUpdate = {}  # type: ignore[typeddict-item]
    if "RecommenderConfig" in data:
        import aws_sdk_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            aws_sdk_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    if "Status" in data:
        import aws_sdk_customer_profiles.types.recommender_status

        out["status"] = (
            aws_sdk_customer_profiles.types.recommender_status.deserialize_json(
                data["Status"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
