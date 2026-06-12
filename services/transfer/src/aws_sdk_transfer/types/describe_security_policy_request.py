"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeSecurityPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.security_policy_name


class DescribeSecurityPolicyRequest(TypedDict):
    security_policy_name: (
        "aws_sdk_transfer.types.security_policy_name.SecurityPolicyName"
    )
    """<p>Specify the text name of the security policy for which you want the details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSecurityPolicyRequest) -> dict:
    out: dict = {}
    out["SecurityPolicyName"] = value["security_policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSecurityPolicyRequest:
    out: DescribeSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
    if "SecurityPolicyName" in data:
        out["security_policy_name"] = data["SecurityPolicyName"]
    else:
        raise DeserializationError(
            "DescribeSecurityPolicyRequest.security_policy_name required"
        )
    return out
