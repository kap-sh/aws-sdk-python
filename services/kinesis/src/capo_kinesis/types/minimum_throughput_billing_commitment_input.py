"""Generated from Smithy shape ``com.amazonaws.kinesis#MinimumThroughputBillingCommitmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.minimum_throughput_billing_commitment_input_status


class MinimumThroughputBillingCommitmentInput(TypedDict, closed=True):
    status: "capo_kinesis.types.minimum_throughput_billing_commitment_input_status.MinimumThroughputBillingCommitmentInputStatus"
    """<p>The desired status of the minimum throughput billing commitment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MinimumThroughputBillingCommitmentInput) -> dict:
    out: dict = {}
    import capo_kinesis.types.minimum_throughput_billing_commitment_input_status

    out["Status"] = (
        capo_kinesis.types.minimum_throughput_billing_commitment_input_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> MinimumThroughputBillingCommitmentInput:
    out: MinimumThroughputBillingCommitmentInput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_kinesis.types.minimum_throughput_billing_commitment_input_status

        out["status"] = (
            capo_kinesis.types.minimum_throughput_billing_commitment_input_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "MinimumThroughputBillingCommitmentInput.status required"
        )
    return out
