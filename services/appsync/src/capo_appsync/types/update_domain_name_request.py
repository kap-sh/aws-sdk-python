"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.description
    import capo_appsync.types.domain_name


class UpdateDomainNameRequest(TypedDict, closed=True):
    domain_name: "capo_appsync.types.domain_name.DomainName"
    """<p>The domain name.</p>"""
    description: NotRequired["capo_appsync.types.description.Description"]
    """<p>A description of the <code>DomainName</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainNameRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateDomainNameRequest:
    out: UpdateDomainNameRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
