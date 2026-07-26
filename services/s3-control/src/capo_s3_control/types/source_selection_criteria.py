"""Generated from Smithy shape ``com.amazonaws.s3control#SourceSelectionCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.replica_modifications
    import capo_s3_control.types.sse_kms_encrypted_objects


class SourceSelectionCriteria(TypedDict, closed=True):
    sse_kms_encrypted_objects: NotRequired[
        "capo_s3_control.types.sse_kms_encrypted_objects.SseKmsEncryptedObjects"
    ]
    """<p>A filter that you can use to select Amazon S3 objects that are encrypted with server-side encryption by using Key Management Service (KMS) keys. If you include <code>SourceSelectionCriteria</code> in the replication configuration, this element is required. </p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    replica_modifications: NotRequired[
        "capo_s3_control.types.replica_modifications.ReplicaModifications"
    ]
    """<p>A filter that you can use to specify whether replica modification sync is enabled. S3 on Outposts replica modification sync can help you keep object metadata synchronized between replicas and source objects. By default, S3 on Outposts replicates metadata from the source objects to the replicas only. When replica modification sync is enabled, S3 on Outposts replicates metadata changes made to the replica copies back to the source object, making the replication bidirectional.</p> <p>To replicate object metadata modifications on replicas, you can specify this element and set the <code>Status</code> of this element to <code>Enabled</code>.</p> <note> <p>You must enable replica modification sync on the source and destination buckets to replicate replica metadata changes between the source and the replicas.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: SourceSelectionCriteria, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "sse_kms_encrypted_objects" in value:
        import capo_s3_control.types.sse_kms_encrypted_objects

        capo_s3_control.types.sse_kms_encrypted_objects.serialize_xml(
            value["sse_kms_encrypted_objects"], el, "SseKmsEncryptedObjects"
        )
    if "replica_modifications" in value:
        import capo_s3_control.types.replica_modifications

        capo_s3_control.types.replica_modifications.serialize_xml(
            value["replica_modifications"], el, "ReplicaModifications"
        )


def deserialize_xml(el: Element) -> SourceSelectionCriteria:
    out: SourceSelectionCriteria = {}  # type: ignore[typeddict-item]
    child_sse_kms_encrypted_objects = el.find("SseKmsEncryptedObjects")
    if child_sse_kms_encrypted_objects is not None:
        import capo_s3_control.types.sse_kms_encrypted_objects

        out["sse_kms_encrypted_objects"] = (
            capo_s3_control.types.sse_kms_encrypted_objects.deserialize_xml(
                child_sse_kms_encrypted_objects
            )
        )
    child_replica_modifications = el.find("ReplicaModifications")
    if child_replica_modifications is not None:
        import capo_s3_control.types.replica_modifications

        out["replica_modifications"] = (
            capo_s3_control.types.replica_modifications.deserialize_xml(
                child_replica_modifications
            )
        )
    return out
