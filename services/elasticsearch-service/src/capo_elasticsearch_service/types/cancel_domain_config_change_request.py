"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CancelDomainConfigChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.dry_run


class CancelDomainConfigChangeRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>Name of the OpenSearch Service domain configuration request to cancel.</p>"""
    dry_run: NotRequired["capo_elasticsearch_service.types.dry_run.DryRun"]
    """<p>When set to <b>True</b>, returns the list of change IDs and properties that will be cancelled without actually cancelling the change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelDomainConfigChangeRequest) -> dict:
    out: dict = {}
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> CancelDomainConfigChangeRequest:
    out: CancelDomainConfigChangeRequest = {}  # type: ignore[typeddict-item]
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    return out
