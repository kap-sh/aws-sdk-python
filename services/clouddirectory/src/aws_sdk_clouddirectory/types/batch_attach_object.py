"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAttachObject``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.object_reference


class BatchAttachObject(TypedDict):
    parent_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The parent object reference.</p>"""
    child_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The child object reference that is to be attached to the object.</p>"""
    link_name: "aws_sdk_clouddirectory.types.link_name.LinkName"
    """<p>The name of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAttachObject) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ParentReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["parent_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.object_reference

    out["ChildReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["child_reference"]
        )
    )
    out["LinkName"] = value["link_name"]
    return out


def deserialize_json(data: dict) -> BatchAttachObject:
    out: BatchAttachObject = {}  # type: ignore[typeddict-item]
    if "ParentReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["parent_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachObject.parent_reference required")
    if "ChildReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["child_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ChildReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachObject.child_reference required")
    if "LinkName" in data:
        out["link_name"] = data["LinkName"]
    else:
        raise DeserializationError("BatchAttachObject.link_name required")
    return out
