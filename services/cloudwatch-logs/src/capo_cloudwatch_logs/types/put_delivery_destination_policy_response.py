"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliveryDestinationPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.policy


class PutDeliveryDestinationPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_cloudwatch_logs.types.policy.Policy"]
    """<p>The contents of the policy that you just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryDestinationPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_cloudwatch_logs.types.policy

        out["policy"] = capo_cloudwatch_logs.types.policy.serialize_aws_json_1_1(
            value["policy"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryDestinationPolicyResponse:
    out: PutDeliveryDestinationPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import capo_cloudwatch_logs.types.policy

        out["policy"] = capo_cloudwatch_logs.types.policy.deserialize_aws_json_1_1(
            data["policy"]
        )
    return out
