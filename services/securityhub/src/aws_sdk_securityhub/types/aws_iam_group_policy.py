"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamGroupPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamGroupPolicy(TypedDict, closed=True):
    policy_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamGroupPolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_json(data: dict) -> AwsIamGroupPolicy:
    out: AwsIamGroupPolicy = {}  # type: ignore[typeddict-item]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    return out
