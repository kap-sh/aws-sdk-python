"""Generated from Smithy shape ``com.amazonaws.kinesis#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.policy


class GetResourcePolicyOutput(TypedDict):
    policy: "aws_sdk_kinesis.types.policy.Policy"
    """<p>Details of the resource policy. This is formatted as a JSON string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyOutput) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyOutput:
    out: GetResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("GetResourcePolicyOutput.policy required")
    return out
