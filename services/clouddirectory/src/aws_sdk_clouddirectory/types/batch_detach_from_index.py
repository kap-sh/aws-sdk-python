"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDetachFromIndex``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_reference


class BatchDetachFromIndex(TypedDict):
    index_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the index object.</p>"""
    target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object being detached from the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDetachFromIndex) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["IndexReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["index_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.object_reference

    out["TargetReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["target_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDetachFromIndex:
    out: BatchDetachFromIndex = {}  # type: ignore[typeddict-item]
    if "IndexReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["index_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["IndexReference"]
            )
        )
    else:
        raise DeserializationError("BatchDetachFromIndex.index_reference required")
    if "TargetReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["target_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["TargetReference"]
            )
        )
    else:
        raise DeserializationError("BatchDetachFromIndex.target_reference required")
    return out
