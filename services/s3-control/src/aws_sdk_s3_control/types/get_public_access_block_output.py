"""Generated from Smithy shape ``com.amazonaws.s3control#GetPublicAccessBlockOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.public_access_block_configuration


class GetPublicAccessBlockOutput(TypedDict, closed=True):
    public_access_block_configuration: NotRequired[
        "aws_sdk_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    ]
    """<p>The <code>PublicAccessBlock</code> configuration currently in effect for this Amazon Web Services account.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetPublicAccessBlockOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "public_access_block_configuration" in value:
        import aws_sdk_s3_control.types.public_access_block_configuration

        aws_sdk_s3_control.types.public_access_block_configuration.serialize_xml(
            value["public_access_block_configuration"],
            el,
            "PublicAccessBlockConfiguration",
        )


def deserialize_xml(el: Element) -> GetPublicAccessBlockOutput:
    out: GetPublicAccessBlockOutput = {}  # type: ignore[typeddict-item]
    child_public_access_block_configuration = el.find("PublicAccessBlockConfiguration")
    if child_public_access_block_configuration is not None:
        import aws_sdk_s3_control.types.public_access_block_configuration

        out["public_access_block_configuration"] = (
            aws_sdk_s3_control.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block_configuration
            )
        )
    return out
