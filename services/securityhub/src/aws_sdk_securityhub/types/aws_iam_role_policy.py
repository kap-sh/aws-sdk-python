"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamRolePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamRolePolicy(TypedDict):
    policy_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamRolePolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_json(data: dict) -> AwsIamRolePolicy:
    out: AwsIamRolePolicy = {}  # type: ignore[typeddict-item]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    return out
