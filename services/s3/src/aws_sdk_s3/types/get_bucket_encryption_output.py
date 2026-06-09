"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketEncryptionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.server_side_encryption_configuration


class GetBucketEncryptionOutput(TypedDict):
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_s3.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]


# --- restXml ser/de ---
def serialize_xml(value: GetBucketEncryptionOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "server_side_encryption_configuration" in value:
        import aws_sdk_s3.types.server_side_encryption_configuration

        aws_sdk_s3.types.server_side_encryption_configuration.serialize_xml(
            value["server_side_encryption_configuration"],
            el,
            "ServerSideEncryptionConfiguration",
        )


def deserialize_xml(el: Element) -> GetBucketEncryptionOutput:
    out: GetBucketEncryptionOutput = {}  # type: ignore[typeddict-item]
    child_server_side_encryption_configuration = el.find(
        "ServerSideEncryptionConfiguration"
    )
    if child_server_side_encryption_configuration is not None:
        import aws_sdk_s3.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_s3.types.server_side_encryption_configuration.deserialize_xml(
                child_server_side_encryption_configuration
            )
        )
    return out
