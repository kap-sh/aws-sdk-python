"""Generated from Smithy shape ``com.amazonaws.s3#SourceSelectionCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.replica_modifications
    import aws_sdk_s3.types.sse_kms_encrypted_objects


class SourceSelectionCriteria(TypedDict, closed=True):
    sse_kms_encrypted_objects: NotRequired[
        "aws_sdk_s3.types.sse_kms_encrypted_objects.SseKmsEncryptedObjects"
    ]
    """<p> A container for filter information for the selection of Amazon S3 objects encrypted with Amazon Web Services KMS. If you include <code>SourceSelectionCriteria</code> in the replication configuration, this element is required. </p>"""
    replica_modifications: NotRequired[
        "aws_sdk_s3.types.replica_modifications.ReplicaModifications"
    ]
    """<p>A filter that you can specify for selections for modifications on replicas. Amazon S3 doesn't replicate replica modifications by default. In the latest version of replication configuration (when <code>Filter</code> is specified), you can specify this element and set the status to <code>Enabled</code> to replicate modifications on replicas. </p> <note> <p> If you don't specify the <code>Filter</code> element, Amazon S3 assumes that the replication configuration is the earlier version, V1. In the earlier version, this element is not allowed</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: SourceSelectionCriteria, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "sse_kms_encrypted_objects" in value:
        import aws_sdk_s3.types.sse_kms_encrypted_objects

        aws_sdk_s3.types.sse_kms_encrypted_objects.serialize_xml(
            value["sse_kms_encrypted_objects"], el, "SseKmsEncryptedObjects"
        )
    if "replica_modifications" in value:
        import aws_sdk_s3.types.replica_modifications

        aws_sdk_s3.types.replica_modifications.serialize_xml(
            value["replica_modifications"], el, "ReplicaModifications"
        )


def deserialize_xml(el: Element) -> SourceSelectionCriteria:
    out: SourceSelectionCriteria = {}  # type: ignore[typeddict-item]
    child_sse_kms_encrypted_objects = el.find("SseKmsEncryptedObjects")
    if child_sse_kms_encrypted_objects is not None:
        import aws_sdk_s3.types.sse_kms_encrypted_objects

        out["sse_kms_encrypted_objects"] = (
            aws_sdk_s3.types.sse_kms_encrypted_objects.deserialize_xml(
                child_sse_kms_encrypted_objects
            )
        )
    child_replica_modifications = el.find("ReplicaModifications")
    if child_replica_modifications is not None:
        import aws_sdk_s3.types.replica_modifications

        out["replica_modifications"] = (
            aws_sdk_s3.types.replica_modifications.deserialize_xml(
                child_replica_modifications
            )
        )
    return out
