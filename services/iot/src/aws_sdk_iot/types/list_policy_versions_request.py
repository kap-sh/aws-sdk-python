"""Generated from Smithy shape ``com.amazonaws.iot#ListPolicyVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name


class ListPolicyVersionsRequest(TypedDict, closed=True):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyVersionsRequest:
    out: ListPolicyVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
