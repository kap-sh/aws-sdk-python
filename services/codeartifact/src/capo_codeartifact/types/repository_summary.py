"""Generated from Smithy shape ``com.amazonaws.codeartifact#RepositorySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.description
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.repository_name
    import capo_codeartifact.types.timestamp


class RepositorySummary(TypedDict, closed=True):
    name: NotRequired["capo_codeartifact.types.repository_name.RepositoryName"]
    """<p> The name of the repository. </p>"""
    administrator_account: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID that manages the repository. </p>"""
    domain_name: NotRequired["capo_codeartifact.types.domain_name.DomainName"]
    """<p> The name of the domain that contains the repository. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    arn: NotRequired["capo_codeartifact.types.arn.Arn"]
    """<p> The ARN of the repository. </p>"""
    description: NotRequired["capo_codeartifact.types.description.Description"]
    """<p> The description of the repository. </p>"""
    created_time: NotRequired["capo_codeartifact.types.timestamp.Timestamp"]
    """<p>A timestamp that represents the date and time the repository was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositorySummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "administrator_account" in value:
        out["administratorAccount"] = value["administrator_account"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_owner" in value:
        out["domainOwner"] = value["domain_owner"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_time" in value:
        import capo_codeartifact.types.timestamp

        out["createdTime"] = capo_codeartifact.types.timestamp.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> RepositorySummary:
    out: RepositorySummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "administratorAccount" in data:
        out["administrator_account"] = data["administratorAccount"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "domainOwner" in data:
        out["domain_owner"] = data["domainOwner"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdTime" in data:
        import capo_codeartifact.types.timestamp

        out["created_time"] = capo_codeartifact.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    return out
