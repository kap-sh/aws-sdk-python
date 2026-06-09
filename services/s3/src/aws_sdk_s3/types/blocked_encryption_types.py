"""Generated from Smithy shape ``com.amazonaws.s3#BlockedEncryptionTypes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.encryption_type_list


class BlockedEncryptionTypes(TypedDict):
    encryption_type: NotRequired[
        "aws_sdk_s3.types.encryption_type_list.EncryptionTypeList"
    ]
    """<p>The object encryption type that you want to block or unblock for an Amazon S3 general purpose bucket.</p> <note> <p>Currently, this parameter only supports blocking or unblocking server side encryption with customer-provided keys (SSE-C). For more information about SSE-C, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html\">Using server-side encryption with customer-provided keys (SSE-C)</a>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: BlockedEncryptionTypes, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "encryption_type" in value:
        import aws_sdk_s3.types.encryption_type_list

        aws_sdk_s3.types.encryption_type_list.serialize_xml_flat(
            value["encryption_type"], el, "EncryptionType"
        )


def deserialize_xml(el: Element) -> BlockedEncryptionTypes:
    out: BlockedEncryptionTypes = {}  # type: ignore[typeddict-item]
    if el.find("EncryptionType") is not None:
        import aws_sdk_s3.types.encryption_type_list

        out["encryption_type"] = (
            aws_sdk_s3.types.encryption_type_list.deserialize_xml_flat(
                el, "EncryptionType"
            )
        )
    return out
