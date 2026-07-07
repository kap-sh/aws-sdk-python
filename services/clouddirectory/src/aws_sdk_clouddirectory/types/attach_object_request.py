"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.object_reference


class AttachObjectRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.</p>"""
    parent_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The parent object reference.</p>"""
    child_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The child object reference to be attached to the object.</p>"""
    link_name: "aws_sdk_clouddirectory.types.link_name.LinkName"
    """<p>The link name with which the child object is attached to the parent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachObjectRequest) -> dict:
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


def deserialize_json(data: dict) -> AttachObjectRequest:
    out: AttachObjectRequest = {}  # type: ignore[typeddict-item]
    if "ParentReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["parent_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    else:
        raise DeserializationError("AttachObjectRequest.parent_reference required")
    if "ChildReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["child_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ChildReference"]
            )
        )
    else:
        raise DeserializationError("AttachObjectRequest.child_reference required")
    if "LinkName" in data:
        out["link_name"] = data["LinkName"]
    else:
        raise DeserializationError("AttachObjectRequest.link_name required")
    return out
