"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDetachFromIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_reference


class BatchDetachFromIndex(TypedDict, closed=True):
    index_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the index object.</p>"""
    target_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object being detached from the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDetachFromIndex) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["IndexReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["index_reference"]
    )
    import capo_clouddirectory.types.object_reference

    out["TargetReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["target_reference"]
    )
    return out


def deserialize_json(data: dict) -> BatchDetachFromIndex:
    out: BatchDetachFromIndex = {}  # type: ignore[typeddict-item]
    if "IndexReference" in data:
        import capo_clouddirectory.types.object_reference

        out["index_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["IndexReference"]
            )
        )
    else:
        raise DeserializationError("BatchDetachFromIndex.index_reference required")
    if "TargetReference" in data:
        import capo_clouddirectory.types.object_reference

        out["target_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["TargetReference"]
            )
        )
    else:
        raise DeserializationError("BatchDetachFromIndex.target_reference required")
    return out
