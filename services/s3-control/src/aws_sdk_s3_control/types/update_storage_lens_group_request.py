"""Generated from Smithy shape ``com.amazonaws.s3control#UpdateStorageLensGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.storage_lens_group
    import aws_sdk_s3_control.types.storage_lens_group_name


class UpdateStorageLensGroupRequest(TypedDict, closed=True):
    name: "aws_sdk_s3_control.types.storage_lens_group_name.StorageLensGroupName"
    """<p> The name of the Storage Lens group that you want to update. </p>"""
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID of the Storage Lens group owner. </p>"""
    storage_lens_group: "aws_sdk_s3_control.types.storage_lens_group.StorageLensGroup"
    """<p> The JSON file that contains the Storage Lens group configuration. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateStorageLensGroupRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.storage_lens_group

    aws_sdk_s3_control.types.storage_lens_group.serialize_xml(
        value["storage_lens_group"], el, "StorageLensGroup"
    )


def deserialize_xml(el: Element) -> UpdateStorageLensGroupRequest:
    out: UpdateStorageLensGroupRequest = {}  # type: ignore[typeddict-item]
    child_storage_lens_group = el.find("StorageLensGroup")
    if child_storage_lens_group is not None:
        import aws_sdk_s3_control.types.storage_lens_group

        out["storage_lens_group"] = (
            aws_sdk_s3_control.types.storage_lens_group.deserialize_xml(
                child_storage_lens_group
            )
        )
    else:
        raise DeserializationError(
            "UpdateStorageLensGroupRequest.storage_lens_group required"
        )
    return out
