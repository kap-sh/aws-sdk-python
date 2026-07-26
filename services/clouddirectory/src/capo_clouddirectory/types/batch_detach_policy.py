"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDetachPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_reference


class BatchDetachPolicy(TypedDict, closed=True):
    policy_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the policy object.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the object whose policy object will be detached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDetachPolicy) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["PolicyReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["policy_reference"]
    )
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    return out


def deserialize_json(data: dict) -> BatchDetachPolicy:
    out: BatchDetachPolicy = {}  # type: ignore[typeddict-item]
    if "PolicyReference" in data:
        import capo_clouddirectory.types.object_reference

        out["policy_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["PolicyReference"]
            )
        )
    else:
        raise DeserializationError("BatchDetachPolicy.policy_reference required")
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("BatchDetachPolicy.object_reference required")
    return out
