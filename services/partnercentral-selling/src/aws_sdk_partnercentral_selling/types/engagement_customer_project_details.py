"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementCustomerProjectDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_customer_business_problem
    import aws_sdk_partnercentral_selling.types.engagement_customer_project_title


class EngagementCustomerProjectDetails(TypedDict):
    title: "aws_sdk_partnercentral_selling.types.engagement_customer_project_title.EngagementCustomerProjectTitle"
    """<p>The title of the project.</p>"""
    business_problem: "aws_sdk_partnercentral_selling.types.engagement_customer_business_problem.EngagementCustomerBusinessProblem"
    """<p>A description of the business problem the project aims to solve.</p>"""
    target_completion_date: "str"
    """<p>The target completion date for the customer's project.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementCustomerProjectDetails) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    out["BusinessProblem"] = value["business_problem"]
    out["TargetCompletionDate"] = value["target_completion_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementCustomerProjectDetails:
    out: EngagementCustomerProjectDetails = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EngagementCustomerProjectDetails.title required")
    if "BusinessProblem" in data:
        out["business_problem"] = data["BusinessProblem"]
    else:
        raise DeserializationError(
            "EngagementCustomerProjectDetails.business_problem required"
        )
    if "TargetCompletionDate" in data:
        out["target_completion_date"] = data["TargetCompletionDate"]
    else:
        raise DeserializationError(
            "EngagementCustomerProjectDetails.target_completion_date required"
        )
    return out
