"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchGetObjectInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_reference


class BatchGetObjectInformation(TypedDict, closed=True):
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetObjectInformation) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetObjectInformation:
    out: BatchGetObjectInformation = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetObjectInformation.object_reference required"
        )
    return out
