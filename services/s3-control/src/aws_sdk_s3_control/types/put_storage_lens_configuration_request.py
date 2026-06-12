"""Generated from Smithy shape ``com.amazonaws.s3control#PutStorageLensConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.config_id
    import aws_sdk_s3_control.types.storage_lens_configuration
    import aws_sdk_s3_control.types.storage_lens_tags


class PutStorageLensConfigurationRequest(TypedDict):
    config_id: "aws_sdk_s3_control.types.config_id.ConfigId"
    """<p>The ID of the S3 Storage Lens configuration.</p>"""
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The account ID of the requester.</p>"""
    storage_lens_configuration: (
        "aws_sdk_s3_control.types.storage_lens_configuration.StorageLensConfiguration"
    )
    """<p>The S3 Storage Lens configuration.</p>"""
    tags: NotRequired["aws_sdk_s3_control.types.storage_lens_tags.StorageLensTags"]
    """<p>The tag set of the S3 Storage Lens configuration.</p> <note> <p>You can set up to a maximum of 50 tags.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutStorageLensConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.storage_lens_configuration

    aws_sdk_s3_control.types.storage_lens_configuration.serialize_xml(
        value["storage_lens_configuration"], el, "StorageLensConfiguration"
    )
    if "tags" in value:
        import aws_sdk_s3_control.types.storage_lens_tags

        aws_sdk_s3_control.types.storage_lens_tags.serialize_xml(
            value["tags"], el, "Tags"
        )


def deserialize_xml(el: Element) -> PutStorageLensConfigurationRequest:
    out: PutStorageLensConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_storage_lens_configuration = el.find("StorageLensConfiguration")
    if child_storage_lens_configuration is not None:
        import aws_sdk_s3_control.types.storage_lens_configuration

        out["storage_lens_configuration"] = (
            aws_sdk_s3_control.types.storage_lens_configuration.deserialize_xml(
                child_storage_lens_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutStorageLensConfigurationRequest.storage_lens_configuration required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_s3_control.types.storage_lens_tags

        out["tags"] = aws_sdk_s3_control.types.storage_lens_tags.deserialize_xml(
            child_tags
        )
    return out
