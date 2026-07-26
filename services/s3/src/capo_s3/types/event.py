"""Generated from Smithy shape ``com.amazonaws.s3#Event``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

"""<p>The bucket event for which to send notifications.</p>"""
Event: TypeAlias = Literal[
    "s3:ReducedRedundancyLostObject",
    "s3:ObjectCreated:*",
    "s3:ObjectCreated:Put",
    "s3:ObjectCreated:Post",
    "s3:ObjectCreated:Copy",
    "s3:ObjectCreated:CompleteMultipartUpload",
    "s3:ObjectRemoved:*",
    "s3:ObjectRemoved:Delete",
    "s3:ObjectRemoved:DeleteMarkerCreated",
    "s3:ObjectRestore:*",
    "s3:ObjectRestore:Post",
    "s3:ObjectRestore:Completed",
    "s3:Replication:*",
    "s3:Replication:OperationFailedReplication",
    "s3:Replication:OperationNotTracked",
    "s3:Replication:OperationMissedThreshold",
    "s3:Replication:OperationReplicatedAfterThreshold",
    "s3:ObjectRestore:Delete",
    "s3:LifecycleTransition",
    "s3:IntelligentTiering",
    "s3:ObjectAcl:Put",
    "s3:LifecycleExpiration:*",
    "s3:LifecycleExpiration:Delete",
    "s3:LifecycleExpiration:DeleteMarkerCreated",
    "s3:ObjectTagging:*",
    "s3:ObjectTagging:Put",
    "s3:ObjectTagging:Delete",
]


# --- restXml ser/de ---
def to_xml_text(value: Event) -> str:
    return value


def from_xml_text(text: str) -> Event:
    return cast(Event, text)


def serialize_xml(value: Event, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Event:
    return from_xml_text(el.text or "")
