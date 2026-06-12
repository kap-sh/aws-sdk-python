"""Generated from Smithy shape ``com.amazonaws.s3control#GetStorageLensGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.storage_lens_group_name


class GetStorageLensGroupRequest(TypedDict):
    name: "aws_sdk_s3_control.types.storage_lens_group_name.StorageLensGroupName"
    """<p> The name of the Storage Lens group that you're trying to retrieve the configuration details for. </p>"""
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID associated with the Storage Lens group that you're trying to retrieve the details for. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetStorageLensGroupRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetStorageLensGroupRequest:
    out: GetStorageLensGroupRequest = {}  # type: ignore[typeddict-item]
    return out
