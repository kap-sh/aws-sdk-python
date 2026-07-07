"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeSecurityPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_security_policy


class DescribeSecurityPolicyResponse(TypedDict, closed=True):
    security_policy: (
        "aws_sdk_transfer.types.described_security_policy.DescribedSecurityPolicy"
    )
    """<p>An array containing the properties of the security policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSecurityPolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.described_security_policy

    out["SecurityPolicy"] = (
        aws_sdk_transfer.types.described_security_policy.serialize_aws_json_1_1(
            value["security_policy"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSecurityPolicyResponse:
    out: DescribeSecurityPolicyResponse = {}  # type: ignore[typeddict-item]
    if "SecurityPolicy" in data:
        import aws_sdk_transfer.types.described_security_policy

        out["security_policy"] = (
            aws_sdk_transfer.types.described_security_policy.deserialize_aws_json_1_1(
                data["SecurityPolicy"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeSecurityPolicyResponse.security_policy required"
        )
    return out
