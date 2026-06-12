"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDeleteObject``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_reference


class BatchDeleteObject(TypedDict):
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteObject) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteObject:
    out: BatchDeleteObject = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteObject.object_reference required")
    return out
