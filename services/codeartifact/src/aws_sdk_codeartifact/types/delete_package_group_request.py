"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeletePackageGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.string


class DeletePackageGroupRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The domain that contains the package group to be deleted. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: "aws_sdk_codeartifact.types.string.String"
    """<p>The pattern of the package group to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageGroupRequest:
    out: DeletePackageGroupRequest = {}  # type: ignore[typeddict-item]
    return out
