"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDetachObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_reference_name
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.object_reference


class BatchDetachObject(TypedDict):
    parent_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>Parent reference from which the object with the specified link name is detached.</p>"""
    link_name: "aws_sdk_clouddirectory.types.link_name.LinkName"
    """<p>The name of the link.</p>"""
    batch_reference_name: NotRequired[
        "aws_sdk_clouddirectory.types.batch_reference_name.BatchReferenceName"
    ]
    r"""<p>The batch reference name. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html\">Transaction Support</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDetachObject) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ParentReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["parent_reference"]
        )
    )
    out["LinkName"] = value["link_name"]
    if "batch_reference_name" in value:
        out["BatchReferenceName"] = value["batch_reference_name"]
    return out


def deserialize_json(data: dict) -> BatchDetachObject:
    out: BatchDetachObject = {}  # type: ignore[typeddict-item]
    if "ParentReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["parent_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    else:
        raise DeserializationError("BatchDetachObject.parent_reference required")
    if "LinkName" in data:
        out["link_name"] = data["LinkName"]
    else:
        raise DeserializationError("BatchDetachObject.link_name required")
    if "BatchReferenceName" in data:
        out["batch_reference_name"] = data["BatchReferenceName"]
    return out
