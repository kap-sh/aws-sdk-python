"""Generated from Smithy shape ``com.amazonaws.codebuild#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class GetResourcePolicyOutput(TypedDict):
    policy: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The resource policy for the resource identified by the input ARN parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyOutput:
    out: GetResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
