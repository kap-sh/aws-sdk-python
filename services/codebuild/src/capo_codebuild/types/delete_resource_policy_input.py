"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class DeleteResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The ARN of the resource that is associated with the resource policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyInput:
    out: DeleteResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyInput.resource_arn required")
    return out
