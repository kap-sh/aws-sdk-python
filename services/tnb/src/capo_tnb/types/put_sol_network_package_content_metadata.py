"""Generated from Smithy shape ``com.amazonaws.tnb#PutSolNetworkPackageContentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.network_artifact_meta


class PutSolNetworkPackageContentMetadata(TypedDict, closed=True):
    nsd: NotRequired["capo_tnb.types.network_artifact_meta.NetworkArtifactMeta"]


# --- restJson1 ser/de ---
def serialize_json(value: PutSolNetworkPackageContentMetadata) -> dict:
    out: dict = {}
    if "nsd" in value:
        import capo_tnb.types.network_artifact_meta

        out["nsd"] = capo_tnb.types.network_artifact_meta.serialize_json(value["nsd"])
    return out


def deserialize_json(data: dict) -> PutSolNetworkPackageContentMetadata:
    out: PutSolNetworkPackageContentMetadata = {}  # type: ignore[typeddict-item]
    if "nsd" in data:
        import capo_tnb.types.network_artifact_meta

        out["nsd"] = capo_tnb.types.network_artifact_meta.deserialize_json(data["nsd"])
    return out
