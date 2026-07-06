"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeAccountSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.minimum_throughput_billing_commitment_output


class DescribeAccountSettingsOutput(TypedDict, closed=True):
    minimum_throughput_billing_commitment: NotRequired[
        "aws_sdk_kinesis.types.minimum_throughput_billing_commitment_output.MinimumThroughputBillingCommitmentOutput"
    ]
    """<p>The current configuration of the minimum throughput billing commitment for your Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountSettingsOutput) -> dict:
    out: dict = {}
    if "minimum_throughput_billing_commitment" in value:
        import aws_sdk_kinesis.types.minimum_throughput_billing_commitment_output

        out["MinimumThroughputBillingCommitment"] = (
            aws_sdk_kinesis.types.minimum_throughput_billing_commitment_output.serialize_aws_json_1_1(
                value["minimum_throughput_billing_commitment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountSettingsOutput:
    out: DescribeAccountSettingsOutput = {}  # type: ignore[typeddict-item]
    if "MinimumThroughputBillingCommitment" in data:
        import aws_sdk_kinesis.types.minimum_throughput_billing_commitment_output

        out["minimum_throughput_billing_commitment"] = (
            aws_sdk_kinesis.types.minimum_throughput_billing_commitment_output.deserialize_aws_json_1_1(
                data["MinimumThroughputBillingCommitment"]
            )
        )
    return out
