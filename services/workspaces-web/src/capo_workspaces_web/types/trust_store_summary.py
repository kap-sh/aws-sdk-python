"""Generated from Smithy shape ``com.amazonaws.workspacesweb#TrustStoreSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class TrustStoreSummary(TypedDict, closed=True):
    trust_store_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustStoreSummary) -> dict:
    out: dict = {}
    if "trust_store_arn" in value:
        out["trustStoreArn"] = value["trust_store_arn"]
    return out


def deserialize_json(data: dict) -> TrustStoreSummary:
    out: TrustStoreSummary = {}  # type: ignore[typeddict-item]
    if "trustStoreArn" in data:
        out["trust_store_arn"] = data["trustStoreArn"]
    return out
