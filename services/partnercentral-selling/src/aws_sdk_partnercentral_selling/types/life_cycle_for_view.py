"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LifeCycleForView``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.date
    import aws_sdk_partnercentral_selling.types.pii_string
    import aws_sdk_partnercentral_selling.types.review_status
    import aws_sdk_partnercentral_selling.types.stage


class LifeCycleForView(TypedDict):
    target_close_date: NotRequired["aws_sdk_partnercentral_selling.types.date.Date"]
    """<p> The projected launch date of the opportunity shared through a snapshot. </p>"""
    review_status: NotRequired[
        "aws_sdk_partnercentral_selling.types.review_status.ReviewStatus"
    ]
    """<p> Defines the approval status of the opportunity shared through a snapshot. </p>"""
    stage: NotRequired["aws_sdk_partnercentral_selling.types.stage.Stage"]
    """<p> Defines the current stage of the opportunity shared through a snapshot. </p>"""
    next_steps: NotRequired["aws_sdk_partnercentral_selling.types.pii_string.PiiString"]
    """<p> Describes the next steps for the opportunity shared through a snapshot. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifeCycleForView) -> dict:
    out: dict = {}
    if "target_close_date" in value:
        out["TargetCloseDate"] = value["target_close_date"]
    if "review_status" in value:
        import aws_sdk_partnercentral_selling.types.review_status

        out["ReviewStatus"] = (
            aws_sdk_partnercentral_selling.types.review_status.serialize_aws_json_1_0(
                value["review_status"]
            )
        )
    if "stage" in value:
        import aws_sdk_partnercentral_selling.types.stage

        out["Stage"] = (
            aws_sdk_partnercentral_selling.types.stage.serialize_aws_json_1_0(
                value["stage"]
            )
        )
    if "next_steps" in value:
        out["NextSteps"] = value["next_steps"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifeCycleForView:
    out: LifeCycleForView = {}  # type: ignore[typeddict-item]
    if "TargetCloseDate" in data:
        out["target_close_date"] = data["TargetCloseDate"]
    if "ReviewStatus" in data:
        import aws_sdk_partnercentral_selling.types.review_status

        out["review_status"] = (
            aws_sdk_partnercentral_selling.types.review_status.deserialize_aws_json_1_0(
                data["ReviewStatus"]
            )
        )
    if "Stage" in data:
        import aws_sdk_partnercentral_selling.types.stage

        out["stage"] = (
            aws_sdk_partnercentral_selling.types.stage.deserialize_aws_json_1_0(
                data["Stage"]
            )
        )
    if "NextSteps" in data:
        out["next_steps"] = data["NextSteps"]
    return out
