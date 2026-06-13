"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_tnb.types.function_artifact_meta


class GetSolFunctionPackageMetadata(TypedDict):
    vnfd: NotRequired["aws_sdk_tnb.types.function_artifact_meta.FunctionArtifactMeta"]
    """<p>Metadata related to the function package descriptor of the function package.</p>"""
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageMetadata) -> dict:
    out: dict = {}
    if "vnfd" in value:
        import aws_sdk_tnb.types.function_artifact_meta

        out["vnfd"] = aws_sdk_tnb.types.function_artifact_meta.serialize_json(
            value["vnfd"]
        )
    import aws_sdk_tnb.types._prelude.timestamp

    out["createdAt"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_tnb.types._prelude.timestamp

    out["lastModified"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageMetadata:
    out: GetSolFunctionPackageMetadata = {}  # type: ignore[typeddict-item]
    if "vnfd" in data:
        import aws_sdk_tnb.types.function_artifact_meta

        out["vnfd"] = aws_sdk_tnb.types.function_artifact_meta.deserialize_json(
            data["vnfd"]
        )
    if "createdAt" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["created_at"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSolFunctionPackageMetadata.created_at required")
    if "lastModified" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["last_modified"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "GetSolFunctionPackageMetadata.last_modified required"
        )
    return out
