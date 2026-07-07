"""Generated from Smithy shape ``com.amazonaws.xray#ListResourcePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.resource_policy_next_token


class ListResourcePoliciesRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_xray.types.resource_policy_next_token.ResourcePolicyNextToken"
    ]
    """<p>Not currently supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePoliciesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcePoliciesRequest:
    out: ListResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
