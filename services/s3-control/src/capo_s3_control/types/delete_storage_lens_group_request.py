"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteStorageLensGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.storage_lens_group_name


class DeleteStorageLensGroupRequest(TypedDict, closed=True):
    name: "capo_s3_control.types.storage_lens_group_name.StorageLensGroupName"
    """<p> The name of the Storage Lens group that you're trying to delete. </p>"""
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID used to create the Storage Lens group that you're trying to delete. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteStorageLensGroupRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteStorageLensGroupRequest:
    out: DeleteStorageLensGroupRequest = {}  # type: ignore[typeddict-item]
    return out
