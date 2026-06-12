"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliveryDestinationPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.policy


class PutDeliveryDestinationPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_cloudwatch_logs.types.policy.Policy"]
    """<p>The contents of the policy that you just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryDestinationPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_cloudwatch_logs.types.policy

        out["policy"] = aws_sdk_cloudwatch_logs.types.policy.serialize_aws_json_1_1(
            value["policy"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryDestinationPolicyResponse:
    out: PutDeliveryDestinationPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_cloudwatch_logs.types.policy

        out["policy"] = aws_sdk_cloudwatch_logs.types.policy.deserialize_aws_json_1_1(
            data["policy"]
        )
    return out
