"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAttachToIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_reference


class BatchAttachToIndex(TypedDict, closed=True):
    index_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the index that you are attaching the object to.</p>"""
    target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object that you are attaching to the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAttachToIndex) -> dict:
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


def deserialize_json(data: dict) -> BatchAttachToIndex:
    out: BatchAttachToIndex = {}  # type: ignore[typeddict-item]
    if "IndexReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["index_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["IndexReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachToIndex.index_reference required")
    if "TargetReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["target_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["TargetReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachToIndex.target_reference required")
    return out
