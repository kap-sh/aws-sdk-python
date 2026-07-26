"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#FilterLifeCycleReviewStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.review_status

FilterLifeCycleReviewStatus: TypeAlias = list[
    "capo_partnercentral_selling.types.review_status.ReviewStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterLifeCycleReviewStatus) -> list:
    import capo_partnercentral_selling.types.review_status

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.review_status.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FilterLifeCycleReviewStatus:
    import capo_partnercentral_selling.types.review_status

    out: FilterLifeCycleReviewStatus = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.review_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
