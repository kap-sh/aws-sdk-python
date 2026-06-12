"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProjectDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.date
    import aws_sdk_partnercentral_selling.types.engagement_customer_business_problem
    import aws_sdk_partnercentral_selling.types.expected_customer_spend_list


class ProjectDetails(TypedDict):
    business_problem: "aws_sdk_partnercentral_selling.types.engagement_customer_business_problem.EngagementCustomerBusinessProblem"
    """<p>Describes the business problem that the project aims to solve. This information is crucial for understanding the project’s goals and objectives.</p>"""
    title: "str"
    """<p>Specifies the title of the project. This title helps partners quickly identify and understand the focus of the project.</p>"""
    target_completion_date: "aws_sdk_partnercentral_selling.types.date.Date"
    """<p>Specifies the estimated date of project completion. This field helps track the project timeline and manage expectations.</p>"""
    expected_customer_spend: "aws_sdk_partnercentral_selling.types.expected_customer_spend_list.ExpectedCustomerSpendList"
    """<p>Contains revenue estimates for the partner related to the project. This field provides an idea of the financial potential of the opportunity for the partner.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectDetails) -> dict:
    out: dict = {}
    out["BusinessProblem"] = value["business_problem"]
    out["Title"] = value["title"]
    out["TargetCompletionDate"] = value["target_completion_date"]
    import aws_sdk_partnercentral_selling.types.expected_customer_spend_list

    out["ExpectedCustomerSpend"] = (
        aws_sdk_partnercentral_selling.types.expected_customer_spend_list.serialize_aws_json_1_0(
            value["expected_customer_spend"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProjectDetails:
    out: ProjectDetails = {}  # type: ignore[typeddict-item]
    if "BusinessProblem" in data:
        out["business_problem"] = data["BusinessProblem"]
    else:
        raise DeserializationError("ProjectDetails.business_problem required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("ProjectDetails.title required")
    if "TargetCompletionDate" in data:
        out["target_completion_date"] = data["TargetCompletionDate"]
    else:
        raise DeserializationError("ProjectDetails.target_completion_date required")
    if "ExpectedCustomerSpend" in data:
        import aws_sdk_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            aws_sdk_partnercentral_selling.types.expected_customer_spend_list.deserialize_aws_json_1_0(
                data["ExpectedCustomerSpend"]
            )
        )
    else:
        raise DeserializationError("ProjectDetails.expected_customer_spend required")
    return out
