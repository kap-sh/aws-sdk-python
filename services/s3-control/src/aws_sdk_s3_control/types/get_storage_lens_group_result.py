"""Generated from Smithy shape ``com.amazonaws.s3control#GetStorageLensGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.storage_lens_group


class GetStorageLensGroupResult(TypedDict, closed=True):
    storage_lens_group: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_group.StorageLensGroup"
    ]
    """<p> The name of the Storage Lens group that you're trying to retrieve the configuration details for. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetStorageLensGroupResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "storage_lens_group" in value:
        import aws_sdk_s3_control.types.storage_lens_group

        aws_sdk_s3_control.types.storage_lens_group.serialize_xml(
            value["storage_lens_group"], el, "StorageLensGroup"
        )


def deserialize_xml(el: Element) -> GetStorageLensGroupResult:
    out: GetStorageLensGroupResult = {}  # type: ignore[typeddict-item]
    child_storage_lens_group = el.find("StorageLensGroup")
    if child_storage_lens_group is not None:
        import aws_sdk_s3_control.types.storage_lens_group

        out["storage_lens_group"] = (
            aws_sdk_s3_control.types.storage_lens_group.deserialize_xml(
                child_storage_lens_group
            )
        )
    return out
