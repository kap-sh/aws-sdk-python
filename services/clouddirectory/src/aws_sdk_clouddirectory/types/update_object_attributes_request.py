"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateObjectAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.object_attribute_update_list
    import aws_sdk_clouddirectory.types.object_reference


class UpdateObjectAttributesRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the object.</p>"""
    attribute_updates: "aws_sdk_clouddirectory.types.object_attribute_update_list.ObjectAttributeUpdateList"
    """<p>The attributes update structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateObjectAttributesRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.object_attribute_update_list

    out["AttributeUpdates"] = (
        aws_sdk_clouddirectory.types.object_attribute_update_list.serialize_json(
            value["attribute_updates"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateObjectAttributesRequest:
    out: UpdateObjectAttributesRequest = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateObjectAttributesRequest.object_reference required"
        )
    if "AttributeUpdates" in data:
        import aws_sdk_clouddirectory.types.object_attribute_update_list

        out["attribute_updates"] = (
            aws_sdk_clouddirectory.types.object_attribute_update_list.deserialize_json(
                data["AttributeUpdates"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateObjectAttributesRequest.attribute_updates required"
        )
    return out
