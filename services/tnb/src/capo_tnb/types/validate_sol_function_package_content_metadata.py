"""Generated from Smithy shape ``com.amazonaws.tnb#ValidateSolFunctionPackageContentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.function_artifact_meta


class ValidateSolFunctionPackageContentMetadata(TypedDict, closed=True):
    vnfd: NotRequired["capo_tnb.types.function_artifact_meta.FunctionArtifactMeta"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSolFunctionPackageContentMetadata) -> dict:
    out: dict = {}
    if "vnfd" in value:
        import capo_tnb.types.function_artifact_meta

        out["vnfd"] = capo_tnb.types.function_artifact_meta.serialize_json(
            value["vnfd"]
        )
    return out


def deserialize_json(data: dict) -> ValidateSolFunctionPackageContentMetadata:
    out: ValidateSolFunctionPackageContentMetadata = {}  # type: ignore[typeddict-item]
    if "vnfd" in data:
        import capo_tnb.types.function_artifact_meta

        out["vnfd"] = capo_tnb.types.function_artifact_meta.deserialize_json(
            data["vnfd"]
        )
    return out
