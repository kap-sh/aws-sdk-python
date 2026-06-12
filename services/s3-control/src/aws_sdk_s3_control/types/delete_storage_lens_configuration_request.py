"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteStorageLensConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.config_id


class DeleteStorageLensConfigurationRequest(TypedDict):
    config_id: "aws_sdk_s3_control.types.config_id.ConfigId"
    """<p>The ID of the S3 Storage Lens configuration.</p>"""
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The account ID of the requester.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteStorageLensConfigurationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteStorageLensConfigurationRequest:
    out: DeleteStorageLensConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
