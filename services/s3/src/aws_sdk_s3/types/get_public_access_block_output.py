"""Generated from Smithy shape ``com.amazonaws.s3#GetPublicAccessBlockOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.public_access_block_configuration


class GetPublicAccessBlockOutput(TypedDict):
    public_access_block_configuration: NotRequired[
        "aws_sdk_s3.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    ]
    """<p>The <code>PublicAccessBlock</code> configuration currently in effect for this Amazon S3 bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetPublicAccessBlockOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "public_access_block_configuration" in value:
        import aws_sdk_s3.types.public_access_block_configuration

        aws_sdk_s3.types.public_access_block_configuration.serialize_xml(
            value["public_access_block_configuration"],
            el,
            "PublicAccessBlockConfiguration",
        )


def deserialize_xml(el: Element) -> GetPublicAccessBlockOutput:
    out: GetPublicAccessBlockOutput = {}  # type: ignore[typeddict-item]
    child_public_access_block_configuration = el.find("PublicAccessBlockConfiguration")
    if child_public_access_block_configuration is not None:
        import aws_sdk_s3.types.public_access_block_configuration

        out["public_access_block_configuration"] = (
            aws_sdk_s3.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block_configuration
            )
        )
    return out
