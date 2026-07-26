"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribeDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name


class DescribeDomainRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> A string that specifies the name of the requested domain. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainRequest:
    out: DescribeDomainRequest = {}  # type: ignore[typeddict-item]
    return out
