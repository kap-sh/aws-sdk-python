"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DetachObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.object_reference


class DetachObjectRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.</p>"""
    parent_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The parent reference from which the object with the specified link name is detached.</p>"""
    link_name: "aws_sdk_clouddirectory.types.link_name.LinkName"
    """<p>The link name associated with the object that needs to be detached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachObjectRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ParentReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["parent_reference"]
        )
    )
    out["LinkName"] = value["link_name"]
    return out


def deserialize_json(data: dict) -> DetachObjectRequest:
    out: DetachObjectRequest = {}  # type: ignore[typeddict-item]
    if "ParentReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["parent_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    else:
        raise DeserializationError("DetachObjectRequest.parent_reference required")
    if "LinkName" in data:
        out["link_name"] = data["LinkName"]
    else:
        raise DeserializationError("DetachObjectRequest.link_name required")
    return out
