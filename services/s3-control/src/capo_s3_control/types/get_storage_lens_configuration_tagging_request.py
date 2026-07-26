"""Generated from Smithy shape ``com.amazonaws.s3control#GetStorageLensConfigurationTaggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.config_id


class GetStorageLensConfigurationTaggingRequest(TypedDict, closed=True):
    config_id: "capo_s3_control.types.config_id.ConfigId"
    """<p>The ID of the Amazon S3 Storage Lens configuration.</p>"""
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID of the requester.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetStorageLensConfigurationTaggingRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetStorageLensConfigurationTaggingRequest:
    out: GetStorageLensConfigurationTaggingRequest = {}  # type: ignore[typeddict-item]
    return out
