"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListPolicyGenerationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.principal_arn
    import capo_accessanalyzer.types.token


class ListPolicyGenerationsRequest(TypedDict, closed=True):
    principal_arn: NotRequired["capo_accessanalyzer.types.principal_arn.PrincipalArn"]
    """<p>The ARN of the IAM entity (user or role) for which you are generating a policy. Use this with <code>ListGeneratedPolicies</code> to filter the results to only include results for a specific principal.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationsRequest:
    out: ListPolicyGenerationsRequest = {}  # type: ignore[typeddict-item]
    return out
