"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateAccountSettingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.minimum_throughput_billing_commitment_input


class UpdateAccountSettingsInput(TypedDict):
    minimum_throughput_billing_commitment: "aws_sdk_kinesis.types.minimum_throughput_billing_commitment_input.MinimumThroughputBillingCommitmentInput"
    """<p>Specifies the minimum throughput billing commitment configuration for your account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAccountSettingsInput) -> dict:
    out: dict = {}
    import aws_sdk_kinesis.types.minimum_throughput_billing_commitment_input

    out["MinimumThroughputBillingCommitment"] = (
        aws_sdk_kinesis.types.minimum_throughput_billing_commitment_input.serialize_aws_json_1_1(
            value["minimum_throughput_billing_commitment"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAccountSettingsInput:
    out: UpdateAccountSettingsInput = {}  # type: ignore[typeddict-item]
    if "MinimumThroughputBillingCommitment" in data:
        import aws_sdk_kinesis.types.minimum_throughput_billing_commitment_input

        out["minimum_throughput_billing_commitment"] = (
            aws_sdk_kinesis.types.minimum_throughput_billing_commitment_input.deserialize_aws_json_1_1(
                data["MinimumThroughputBillingCommitment"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccountSettingsInput.minimum_throughput_billing_commitment required"
        )
    return out
