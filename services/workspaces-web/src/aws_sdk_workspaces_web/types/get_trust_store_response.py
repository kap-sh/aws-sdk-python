"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetTrustStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.trust_store


class GetTrustStoreResponse(TypedDict, closed=True):
    trust_store: NotRequired["aws_sdk_workspaces_web.types.trust_store.TrustStore"]
    """<p>The trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrustStoreResponse) -> dict:
    out: dict = {}
    if "trust_store" in value:
        import aws_sdk_workspaces_web.types.trust_store

        out["trustStore"] = aws_sdk_workspaces_web.types.trust_store.serialize_json(
            value["trust_store"]
        )
    return out


def deserialize_json(data: dict) -> GetTrustStoreResponse:
    out: GetTrustStoreResponse = {}  # type: ignore[typeddict-item]
    if "trustStore" in data:
        import aws_sdk_workspaces_web.types.trust_store

        out["trust_store"] = aws_sdk_workspaces_web.types.trust_store.deserialize_json(
            data["trustStore"]
        )
    return out
