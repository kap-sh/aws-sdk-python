"""Generated from Smithy shape ``com.amazonaws.s3control#GetBucketReplicationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.replication_configuration


class GetBucketReplicationResult(TypedDict):
    replication_configuration: NotRequired[
        "aws_sdk_s3_control.types.replication_configuration.ReplicationConfiguration"
    ]
    """<p>A container for one or more replication rules. A replication configuration must have at least one rule and you can add up to 100 rules. The maximum size of a replication configuration is 128 KB.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketReplicationResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "replication_configuration" in value:
        import aws_sdk_s3_control.types.replication_configuration

        aws_sdk_s3_control.types.replication_configuration.serialize_xml(
            value["replication_configuration"], el, "ReplicationConfiguration"
        )


def deserialize_xml(el: Element) -> GetBucketReplicationResult:
    out: GetBucketReplicationResult = {}  # type: ignore[typeddict-item]
    child_replication_configuration = el.find("ReplicationConfiguration")
    if child_replication_configuration is not None:
        import aws_sdk_s3_control.types.replication_configuration

        out["replication_configuration"] = (
            aws_sdk_s3_control.types.replication_configuration.deserialize_xml(
                child_replication_configuration
            )
        )
    return out
