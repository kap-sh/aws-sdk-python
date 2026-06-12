"""Generated from Smithy shape ``com.amazonaws.organizations#DescribePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.policy


class DescribePolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_organizations.types.policy.Policy"]
    """<p>A structure that contains details about the specified policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_organizations.types.policy

        out["Policy"] = aws_sdk_organizations.types.policy.serialize_aws_json_1_1(
            value["policy"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePolicyResponse:
    out: DescribePolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_organizations.types.policy

        out["policy"] = aws_sdk_organizations.types.policy.deserialize_aws_json_1_1(
            data["Policy"]
        )
    return out
