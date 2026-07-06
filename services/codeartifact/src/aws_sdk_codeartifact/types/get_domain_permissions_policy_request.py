"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetDomainPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name


class GetDomainPermissionsPolicyRequest(TypedDict, closed=True):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain to which the resource policy is attached. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainPermissionsPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainPermissionsPolicyRequest:
    out: GetDomainPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
