"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class DeleteTrustStoreRequest(TypedDict, closed=True):
    trust_store_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTrustStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTrustStoreRequest:
    out: DeleteTrustStoreRequest = {}  # type: ignore[typeddict-item]
    return out
