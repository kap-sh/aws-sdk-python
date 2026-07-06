"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.code
    import aws_sdk_compute_optimizer.types.identifier
    import aws_sdk_compute_optimizer.types.idle_recommendation_resource_type
    import aws_sdk_compute_optimizer.types.message


class IdleRecommendationError(TypedDict, closed=True):
    identifier: NotRequired["aws_sdk_compute_optimizer.types.identifier.Identifier"]
    """<p>The ID of the error.</p>"""
    code: NotRequired["aws_sdk_compute_optimizer.types.code.Code"]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_compute_optimizer.types.message.Message"]
    """<p>The error message.</p>"""
    resource_type: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_recommendation_resource_type.IdleRecommendationResourceType"
    ]
    """<p>The type of resource associated with the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendationError) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_type" in value:
        import aws_sdk_compute_optimizer.types.idle_recommendation_resource_type

        out["resourceType"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleRecommendationError:
    out: IdleRecommendationError = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceType" in data:
        import aws_sdk_compute_optimizer.types.idle_recommendation_resource_type

        out["resource_type"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    return out
