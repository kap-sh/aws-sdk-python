"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CustomerProjectsContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_customer
    import aws_sdk_partnercentral_selling.types.engagement_customer_project_details


class CustomerProjectsContext(TypedDict):
    customer: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_customer.EngagementCustomer"
    ]
    project: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_customer_project_details.EngagementCustomerProjectDetails"
    ]
    """<p>Information about the customer project associated with the Engagement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomerProjectsContext) -> dict:
    out: dict = {}
    if "customer" in value:
        import aws_sdk_partnercentral_selling.types.engagement_customer

        out["Customer"] = (
            aws_sdk_partnercentral_selling.types.engagement_customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import aws_sdk_partnercentral_selling.types.engagement_customer_project_details

        out["Project"] = (
            aws_sdk_partnercentral_selling.types.engagement_customer_project_details.serialize_aws_json_1_0(
                value["project"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomerProjectsContext:
    out: CustomerProjectsContext = {}  # type: ignore[typeddict-item]
    if "Customer" in data:
        import aws_sdk_partnercentral_selling.types.engagement_customer

        out["customer"] = (
            aws_sdk_partnercentral_selling.types.engagement_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if "Project" in data:
        import aws_sdk_partnercentral_selling.types.engagement_customer_project_details

        out["project"] = (
            aws_sdk_partnercentral_selling.types.engagement_customer_project_details.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    return out
