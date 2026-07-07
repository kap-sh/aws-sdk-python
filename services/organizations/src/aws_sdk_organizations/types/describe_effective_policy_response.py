"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeEffectivePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.effective_policy


class DescribeEffectivePolicyResponse(TypedDict, closed=True):
    effective_policy: NotRequired[
        "aws_sdk_organizations.types.effective_policy.EffectivePolicy"
    ]
    """<p>The contents of the effective policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEffectivePolicyResponse) -> dict:
    out: dict = {}
    if "effective_policy" in value:
        import aws_sdk_organizations.types.effective_policy

        out["EffectivePolicy"] = (
            aws_sdk_organizations.types.effective_policy.serialize_aws_json_1_1(
                value["effective_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEffectivePolicyResponse:
    out: DescribeEffectivePolicyResponse = {}  # type: ignore[typeddict-item]
    if "EffectivePolicy" in data:
        import aws_sdk_organizations.types.effective_policy

        out["effective_policy"] = (
            aws_sdk_organizations.types.effective_policy.deserialize_aws_json_1_1(
                data["EffectivePolicy"]
            )
        )
    return out
