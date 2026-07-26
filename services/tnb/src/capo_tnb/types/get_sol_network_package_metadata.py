"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_tnb.types.network_artifact_meta


class GetSolNetworkPackageMetadata(TypedDict, closed=True):
    nsd: NotRequired["capo_tnb.types.network_artifact_meta.NetworkArtifactMeta"]
    """<p>Metadata related to the onboarded network service descriptor in the network package.</p>"""
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageMetadata) -> dict:
    out: dict = {}
    if "nsd" in value:
        import capo_tnb.types.network_artifact_meta

        out["nsd"] = capo_tnb.types.network_artifact_meta.serialize_json(value["nsd"])
    import capo_tnb.types._prelude.timestamp

    out["createdAt"] = capo_tnb.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_tnb.types._prelude.timestamp

    out["lastModified"] = capo_tnb.types._prelude.timestamp.serialize_json(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageMetadata:
    out: GetSolNetworkPackageMetadata = {}  # type: ignore[typeddict-item]
    if "nsd" in data:
        import capo_tnb.types.network_artifact_meta

        out["nsd"] = capo_tnb.types.network_artifact_meta.deserialize_json(data["nsd"])
    if "createdAt" in data:
        import capo_tnb.types._prelude.timestamp

        out["created_at"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSolNetworkPackageMetadata.created_at required")
    if "lastModified" in data:
        import capo_tnb.types._prelude.timestamp

        out["last_modified"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "GetSolNetworkPackageMetadata.last_modified required"
        )
    return out
