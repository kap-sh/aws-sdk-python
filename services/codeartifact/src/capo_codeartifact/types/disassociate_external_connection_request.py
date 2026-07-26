"""Generated from Smithy shape ``com.amazonaws.codeartifact#DisassociateExternalConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.external_connection_name
    import capo_codeartifact.types.repository_name


class DisassociateExternalConnectionRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p>The name of the domain that contains the repository from which to remove the external repository. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p>The name of the repository from which the external connection will be removed. </p>"""
    external_connection: (
        "capo_codeartifact.types.external_connection_name.ExternalConnectionName"
    )
    """<p>The name of the external connection to be removed from the repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateExternalConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateExternalConnectionRequest:
    out: DisassociateExternalConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
