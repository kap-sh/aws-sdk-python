"""Generated from Smithy shape ``com.amazonaws.s3control#CreateStorageLensGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.storage_lens_group
    import aws_sdk_s3_control.types.tag_list


class CreateStorageLensGroupRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID that the Storage Lens group is created from and associated with. </p>"""
    storage_lens_group: "aws_sdk_s3_control.types.storage_lens_group.StorageLensGroup"
    """<p> The Storage Lens group configuration. </p>"""
    tags: NotRequired["aws_sdk_s3_control.types.tag_list.TagList"]
    """<p> The Amazon Web Services resource tags that you're adding to your Storage Lens group. This parameter is optional. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateStorageLensGroupRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.storage_lens_group

    aws_sdk_s3_control.types.storage_lens_group.serialize_xml(
        value["storage_lens_group"], el, "StorageLensGroup"
    )
    if "tags" in value:
        import aws_sdk_s3_control.types.tag_list

        aws_sdk_s3_control.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateStorageLensGroupRequest:
    out: CreateStorageLensGroupRequest = {}  # type: ignore[typeddict-item]
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
            "CreateStorageLensGroupRequest.storage_lens_group required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_s3_control.types.tag_list

        out["tags"] = aws_sdk_s3_control.types.tag_list.deserialize_xml(child_tags)
    return out
