"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityProject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_partition
    import aws_sdk_partnercentral_selling.types.expected_customer_spend_list


class AwsOpportunityProject(TypedDict):
    expected_customer_spend: NotRequired[
        "aws_sdk_partnercentral_selling.types.expected_customer_spend_list.ExpectedCustomerSpendList"
    ]
    r"""<p>Indicates the expected spending by the customer over the course of the project. This value helps partners and AWS estimate the financial impact of the opportunity. Use the <a href=\"https://calculator.aws/#/\">AWS Pricing Calculator</a> to create an estimate of the customer’s total spend. If only annual recurring revenue (ARR) is available, distribute it across 12 months to provide an average monthly value.</p>"""
    aws_partition: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_partition.AwsPartition"
    ]
    """<p>AWS partition where the opportunity will be deployed. Possible values: <code>aws-eusc</code> for AWS European Sovereign Cloud, <code>null</code> for all other partitions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityProject) -> dict:
    out: dict = {}
    if "expected_customer_spend" in value:
        import aws_sdk_partnercentral_selling.types.expected_customer_spend_list

        out["ExpectedCustomerSpend"] = (
            aws_sdk_partnercentral_selling.types.expected_customer_spend_list.serialize_aws_json_1_0(
                value["expected_customer_spend"]
            )
        )
    if "aws_partition" in value:
        import aws_sdk_partnercentral_selling.types.aws_partition

        out["AwsPartition"] = (
            aws_sdk_partnercentral_selling.types.aws_partition.serialize_aws_json_1_0(
                value["aws_partition"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunityProject:
    out: AwsOpportunityProject = {}  # type: ignore[typeddict-item]
    if "ExpectedCustomerSpend" in data:
        import aws_sdk_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            aws_sdk_partnercentral_selling.types.expected_customer_spend_list.deserialize_aws_json_1_0(
                data["ExpectedCustomerSpend"]
            )
        )
    if "AwsPartition" in data:
        import aws_sdk_partnercentral_selling.types.aws_partition

        out["aws_partition"] = (
            aws_sdk_partnercentral_selling.types.aws_partition.deserialize_aws_json_1_0(
                data["AwsPartition"]
            )
        )
    return out
