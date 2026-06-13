"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingInferredMetadataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.string_map


class GetRestoreTestingInferredMetadataOutput(TypedDict):
    inferred_metadata: "aws_sdk_backup.types.string_map.stringMap"
    """<p>This is a string map of the metadata inferred from the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingInferredMetadataOutput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.string_map

    out["InferredMetadata"] = aws_sdk_backup.types.string_map.serialize_json(
        value["inferred_metadata"]
    )
    return out


def deserialize_json(data: dict) -> GetRestoreTestingInferredMetadataOutput:
    out: GetRestoreTestingInferredMetadataOutput = {}  # type: ignore[typeddict-item]
    if "InferredMetadata" in data:
        import aws_sdk_backup.types.string_map

        out["inferred_metadata"] = aws_sdk_backup.types.string_map.deserialize_json(
            data["InferredMetadata"]
        )
    else:
        raise DeserializationError(
            "GetRestoreTestingInferredMetadataOutput.inferred_metadata required"
        )
    return out
