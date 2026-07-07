"""Generated from Smithy shape ``com.amazonaws.opensearch#CancelDomainConfigChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.dry_run


class CancelDomainConfigChangeRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    dry_run: NotRequired["aws_sdk_opensearch.types.dry_run.DryRun"]
    """<p>When set to <code>True</code>, returns the list of change IDs and properties that will be cancelled without actually cancelling the change.</p>"""


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
