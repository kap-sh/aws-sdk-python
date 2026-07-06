"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketReplicationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.replication_configuration


class GetBucketReplicationOutput(TypedDict, closed=True):
    replication_configuration: NotRequired[
        "aws_sdk_s3.types.replication_configuration.ReplicationConfiguration"
    ]


# --- restXml ser/de ---
def serialize_xml(value: GetBucketReplicationOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "replication_configuration" in value:
        import aws_sdk_s3.types.replication_configuration

        aws_sdk_s3.types.replication_configuration.serialize_xml(
            value["replication_configuration"], el, "ReplicationConfiguration"
        )


def deserialize_xml(el: Element) -> GetBucketReplicationOutput:
    out: GetBucketReplicationOutput = {}  # type: ignore[typeddict-item]
    child_replication_configuration = el.find("ReplicationConfiguration")
    if child_replication_configuration is not None:
        import aws_sdk_s3.types.replication_configuration

        out["replication_configuration"] = (
            aws_sdk_s3.types.replication_configuration.deserialize_xml(
                child_replication_configuration
            )
        )
    return out
