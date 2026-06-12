"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAttachPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_reference


class BatchAttachPolicy(TypedDict):
    policy_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that is associated with the policy object.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the object to which the policy will be attached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAttachPolicy) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["PolicyReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["policy_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchAttachPolicy:
    out: BatchAttachPolicy = {}  # type: ignore[typeddict-item]
    if "PolicyReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["policy_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["PolicyReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachPolicy.policy_reference required")
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachPolicy.object_reference required")
    return out
