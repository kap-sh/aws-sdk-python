"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeletePackageGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.string


class DeletePackageGroupRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The domain that contains the package group to be deleted. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: "capo_codeartifact.types.string.String"
    """<p>The pattern of the package group to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageGroupRequest:
    out: DeletePackageGroupRequest = {}  # type: ignore[typeddict-item]
    return out
