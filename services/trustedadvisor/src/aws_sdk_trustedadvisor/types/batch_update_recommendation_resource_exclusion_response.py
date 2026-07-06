"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#BatchUpdateRecommendationResourceExclusionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error_list


class BatchUpdateRecommendationResourceExclusionResponse(TypedDict, closed=True):
    batch_update_recommendation_resource_exclusion_errors: "aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error_list.UpdateRecommendationResourceExclusionErrorList"
    """<p>A list of recommendation resource ARNs whose exclusion status failed to update, if any</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationResourceExclusionResponse) -> dict:
    out: dict = {}
    import aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error_list

    out["batchUpdateRecommendationResourceExclusionErrors"] = (
        aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error_list.serialize_json(
            value["batch_update_recommendation_resource_exclusion_errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateRecommendationResourceExclusionResponse:
    out: BatchUpdateRecommendationResourceExclusionResponse = {}  # type: ignore[typeddict-item]
    if "batchUpdateRecommendationResourceExclusionErrors" in data:
        import aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error_list

        out["batch_update_recommendation_resource_exclusion_errors"] = (
            aws_sdk_trustedadvisor.types.update_recommendation_resource_exclusion_error_list.deserialize_json(
                data["batchUpdateRecommendationResourceExclusionErrors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationResourceExclusionResponse.batch_update_recommendation_resource_exclusion_errors required"
        )
    return out
