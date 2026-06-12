"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.storage_lens_group_arn
    import aws_sdk_s3_control.types.storage_lens_group_filter
    import aws_sdk_s3_control.types.storage_lens_group_name


class StorageLensGroup(TypedDict):
    name: "aws_sdk_s3_control.types.storage_lens_group_name.StorageLensGroupName"
    """<p> Contains the name of the Storage Lens group. </p>"""
    filter: "aws_sdk_s3_control.types.storage_lens_group_filter.StorageLensGroupFilter"
    """<p>Sets the criteria for the Storage Lens group data that is displayed. For multiple filter conditions, the <code>AND</code> or <code>OR</code> logical operator is used.</p>"""
    storage_lens_group_arn: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_group_arn.StorageLensGroupArn"
    ]
    """<p> Contains the Amazon Resource Name (ARN) of the Storage Lens group. This property is read-only. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: StorageLensGroup, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import aws_sdk_s3_control.types.storage_lens_group_filter

    aws_sdk_s3_control.types.storage_lens_group_filter.serialize_xml(
        value["filter"], el, "Filter"
    )
    if "storage_lens_group_arn" in value:
        SubElement(el, "StorageLensGroupArn").text = str(
            value["storage_lens_group_arn"]
        )


def deserialize_xml(el: Element) -> StorageLensGroup:
    out: StorageLensGroup = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("StorageLensGroup.name required")
    child_filter = el.find("Filter")
    if child_filter is not None:
        import aws_sdk_s3_control.types.storage_lens_group_filter

        out["filter"] = (
            aws_sdk_s3_control.types.storage_lens_group_filter.deserialize_xml(
                child_filter
            )
        )
    else:
        raise DeserializationError("StorageLensGroup.filter required")
    child_storage_lens_group_arn = el.find("StorageLensGroupArn")
    if child_storage_lens_group_arn is not None:
        out["storage_lens_group_arn"] = str(child_storage_lens_group_arn.text or "")
    return out
