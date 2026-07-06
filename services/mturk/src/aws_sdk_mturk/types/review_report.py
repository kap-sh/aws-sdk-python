"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.review_action_detail_list
    import aws_sdk_mturk.types.review_result_detail_list


class ReviewReport(TypedDict, closed=True):
    review_results: NotRequired[
        "aws_sdk_mturk.types.review_result_detail_list.ReviewResultDetailList"
    ]
    """<p> A list of ReviewResults objects for each action specified in the Review Policy. </p>"""
    review_actions: NotRequired[
        "aws_sdk_mturk.types.review_action_detail_list.ReviewActionDetailList"
    ]
    """<p> A list of ReviewAction objects for each action specified in the Review Policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewReport) -> dict:
    out: dict = {}
    if "review_results" in value:
        import aws_sdk_mturk.types.review_result_detail_list

        out["ReviewResults"] = (
            aws_sdk_mturk.types.review_result_detail_list.serialize_aws_json_1_1(
                value["review_results"]
            )
        )
    if "review_actions" in value:
        import aws_sdk_mturk.types.review_action_detail_list

        out["ReviewActions"] = (
            aws_sdk_mturk.types.review_action_detail_list.serialize_aws_json_1_1(
                value["review_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReviewReport:
    out: ReviewReport = {}  # type: ignore[typeddict-item]
    if "ReviewResults" in data:
        import aws_sdk_mturk.types.review_result_detail_list

        out["review_results"] = (
            aws_sdk_mturk.types.review_result_detail_list.deserialize_aws_json_1_1(
                data["ReviewResults"]
            )
        )
    if "ReviewActions" in data:
        import aws_sdk_mturk.types.review_action_detail_list

        out["review_actions"] = (
            aws_sdk_mturk.types.review_action_detail_list.deserialize_aws_json_1_1(
                data["ReviewActions"]
            )
        )
    return out
