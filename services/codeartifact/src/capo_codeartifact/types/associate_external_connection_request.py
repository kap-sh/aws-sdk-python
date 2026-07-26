"""Generated from Smithy shape ``com.amazonaws.codeartifact#AssociateExternalConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.external_connection_name
    import capo_codeartifact.types.repository_name


class AssociateExternalConnectionRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p>The name of the domain that contains the repository.</p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository to which the external connection is added. </p>"""
    external_connection: (
        "capo_codeartifact.types.external_connection_name.ExternalConnectionName"
    )
    """<p> The name of the external connection to add to the repository. The following values are supported: </p> <ul> <li> <p> <code>public:npmjs</code> - for the npm public repository. </p> </li> <li> <p> <code>public:nuget-org</code> - for the NuGet Gallery. </p> </li> <li> <p> <code>public:pypi</code> - for the Python Package Index. </p> </li> <li> <p> <code>public:maven-central</code> - for Maven Central. </p> </li> <li> <p> <code>public:maven-googleandroid</code> - for the Google Android repository. </p> </li> <li> <p> <code>public:maven-gradleplugins</code> - for the Gradle plugins repository. </p> </li> <li> <p> <code>public:maven-commonsware</code> - for the CommonsWare Android repository. </p> </li> <li> <p> <code>public:maven-clojars</code> - for the Clojars repository. </p> </li> <li> <p> <code>public:ruby-gems-org</code> - for RubyGems.org. </p> </li> <li> <p> <code>public:crates-io</code> - for Crates.io. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateExternalConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateExternalConnectionRequest:
    out: AssociateExternalConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
