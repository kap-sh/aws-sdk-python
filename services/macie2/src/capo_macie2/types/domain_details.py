"""Generated from Smithy shape ``com.amazonaws.macie2#DomainDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class DomainDetails(TypedDict, closed=True):
    domain_name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainDetails) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> DomainDetails:
    out: DomainDetails = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    return out
