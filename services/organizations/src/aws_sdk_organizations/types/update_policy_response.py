"""Generated from Smithy shape ``com.amazonaws.organizations#UpdatePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.policy


class UpdatePolicyResponse(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_organizations.types.policy.Policy"]
    """<p>A structure that contains details about the updated policy, showing the requested changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_organizations.types.policy

        out["Policy"] = aws_sdk_organizations.types.policy.serialize_aws_json_1_1(
            value["policy"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePolicyResponse:
    out: UpdatePolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_organizations.types.policy

        out["policy"] = aws_sdk_organizations.types.policy.deserialize_aws_json_1_1(
            data["Policy"]
        )
    return out
