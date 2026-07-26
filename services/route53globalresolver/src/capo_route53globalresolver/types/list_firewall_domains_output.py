"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListFirewallDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.domains


class ListFirewallDomainsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    domains: "capo_route53globalresolver.types.domains.Domains"
    """<p>List of domains in the specified domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFirewallDomainsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.domains

    out["domains"] = capo_route53globalresolver.types.domains.serialize_json(
        value["domains"]
    )
    return out


def deserialize_json(data: dict) -> ListFirewallDomainsOutput:
    out: ListFirewallDomainsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "domains" in data:
        import capo_route53globalresolver.types.domains

        out["domains"] = capo_route53globalresolver.types.domains.deserialize_json(
            data["domains"]
        )
    else:
        raise DeserializationError("ListFirewallDomainsOutput.domains required")
    return out
