"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAccessPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class DescribeAccessPolicyRequest(TypedDict):
    access_policy_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the access policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccessPolicyRequest:
    out: DescribeAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
