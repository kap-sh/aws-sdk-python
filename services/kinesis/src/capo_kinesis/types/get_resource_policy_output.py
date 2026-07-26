"""Generated from Smithy shape ``com.amazonaws.kinesis#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.policy


class GetResourcePolicyOutput(TypedDict, closed=True):
    policy: "capo_kinesis.types.policy.Policy"
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
