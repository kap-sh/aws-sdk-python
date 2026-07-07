"""Generated from Smithy shape ``com.amazonaws.mpa#ListPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policies
    import aws_sdk_mpa.types.token


class ListPoliciesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    policies: NotRequired["aws_sdk_mpa.types.policies.Policies"]
    """<p>An array of <code>Policy</code> objects. Contains a list of policies that define the permissions for team resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "policies" in value:
        import aws_sdk_mpa.types.policies

        out["Policies"] = aws_sdk_mpa.types.policies.serialize_json(value["policies"])
    return out


def deserialize_json(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Policies" in data:
        import aws_sdk_mpa.types.policies

        out["policies"] = aws_sdk_mpa.types.policies.deserialize_json(data["Policies"])
    return out
