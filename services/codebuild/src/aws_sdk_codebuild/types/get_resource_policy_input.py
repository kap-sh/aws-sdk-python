"""Generated from Smithy shape ``com.amazonaws.codebuild#GetResourcePolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class GetResourcePolicyInput(TypedDict):
    resource_arn: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The ARN of the resource that is associated with the resource policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyInput:
    out: GetResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyInput.resource_arn required")
    return out
