"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestGeneratorFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.boolean
    import aws_sdk_s3_control.types.key_name_constraint
    import aws_sdk_s3_control.types.object_creation_time
    import aws_sdk_s3_control.types.object_encryption_filter_list
    import aws_sdk_s3_control.types.object_size_greater_than_bytes
    import aws_sdk_s3_control.types.object_size_less_than_bytes
    import aws_sdk_s3_control.types.replication_status_filter_list
    import aws_sdk_s3_control.types.storage_class_list


class JobManifestGeneratorFilter(TypedDict):
    eligible_for_replication: NotRequired["aws_sdk_s3_control.types.boolean.Boolean"]
    """<p>Include objects in the generated manifest only if they are eligible for replication according to the Replication configuration on the source bucket.</p>"""
    created_after: NotRequired[
        "aws_sdk_s3_control.types.object_creation_time.ObjectCreationTime"
    ]
    """<p>If provided, the generated manifest includes only source bucket objects that were created after this time.</p>"""
    created_before: NotRequired[
        "aws_sdk_s3_control.types.object_creation_time.ObjectCreationTime"
    ]
    """<p>If provided, the generated manifest includes only source bucket objects that were created before this time.</p>"""
    object_replication_statuses: NotRequired[
        "aws_sdk_s3_control.types.replication_status_filter_list.ReplicationStatusFilterList"
    ]
    """<p>If provided, the generated manifest includes only source bucket objects that have one of the specified Replication statuses.</p>"""
    key_name_constraint: NotRequired[
        "aws_sdk_s3_control.types.key_name_constraint.KeyNameConstraint"
    ]
    """<p>If provided, the generated manifest includes only source bucket objects whose object keys match the string constraints specified for <code>MatchAnyPrefix</code>, <code>MatchAnySuffix</code>, and <code>MatchAnySubstring</code>.</p>"""
    object_size_greater_than_bytes: NotRequired[
        "aws_sdk_s3_control.types.object_size_greater_than_bytes.ObjectSizeGreaterThanBytes"
    ]
    """<p>If provided, the generated manifest includes only source bucket objects whose file size is greater than the specified number of bytes.</p>"""
    object_size_less_than_bytes: NotRequired[
        "aws_sdk_s3_control.types.object_size_less_than_bytes.ObjectSizeLessThanBytes"
    ]
    """<p>If provided, the generated manifest includes only source bucket objects whose file size is less than the specified number of bytes.</p>"""
    match_any_storage_class: NotRequired[
        "aws_sdk_s3_control.types.storage_class_list.StorageClassList"
    ]
    """<p>If provided, the generated manifest includes only source bucket objects that are stored with the specified storage class.</p>"""
    match_any_object_encryption: NotRequired[
        "aws_sdk_s3_control.types.object_encryption_filter_list.ObjectEncryptionFilterList"
    ]
    """<p>If provided, the generated object list includes only source bucket objects with the indicated server-side encryption type (SSE-S3, SSE-KMS, DSSE-KMS, SSE-C, or NOT-SSE).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobManifestGeneratorFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "eligible_for_replication" in value:
        SubElement(el, "EligibleForReplication").text = (
            "true" if value["eligible_for_replication"] else "false"
        )
    if "created_after" in value:
        import aws_sdk_s3_control.types.object_creation_time

        aws_sdk_s3_control.types.object_creation_time.serialize_xml(
            value["created_after"], el, "CreatedAfter"
        )
    if "created_before" in value:
        import aws_sdk_s3_control.types.object_creation_time

        aws_sdk_s3_control.types.object_creation_time.serialize_xml(
            value["created_before"], el, "CreatedBefore"
        )
    if "object_replication_statuses" in value:
        import aws_sdk_s3_control.types.replication_status_filter_list

        aws_sdk_s3_control.types.replication_status_filter_list.serialize_xml(
            value["object_replication_statuses"], el, "ObjectReplicationStatuses"
        )
    if "key_name_constraint" in value:
        import aws_sdk_s3_control.types.key_name_constraint

        aws_sdk_s3_control.types.key_name_constraint.serialize_xml(
            value["key_name_constraint"], el, "KeyNameConstraint"
        )
    if "object_size_greater_than_bytes" in value:
        SubElement(el, "ObjectSizeGreaterThanBytes").text = str(
            value["object_size_greater_than_bytes"]
        )
    if "object_size_less_than_bytes" in value:
        SubElement(el, "ObjectSizeLessThanBytes").text = str(
            value["object_size_less_than_bytes"]
        )
    if "match_any_storage_class" in value:
        import aws_sdk_s3_control.types.storage_class_list

        aws_sdk_s3_control.types.storage_class_list.serialize_xml(
            value["match_any_storage_class"], el, "MatchAnyStorageClass"
        )
    if "match_any_object_encryption" in value:
        import aws_sdk_s3_control.types.object_encryption_filter_list

        aws_sdk_s3_control.types.object_encryption_filter_list.serialize_xml(
            value["match_any_object_encryption"], el, "MatchAnyObjectEncryption"
        )


def deserialize_xml(el: Element) -> JobManifestGeneratorFilter:
    out: JobManifestGeneratorFilter = {}  # type: ignore[typeddict-item]
    child_eligible_for_replication = el.find("EligibleForReplication")
    if child_eligible_for_replication is not None:
        out["eligible_for_replication"] = (
            child_eligible_for_replication.text or ""
        ).lower() == "true"
    child_created_after = el.find("CreatedAfter")
    if child_created_after is not None:
        import aws_sdk_s3_control.types.object_creation_time

        out["created_after"] = (
            aws_sdk_s3_control.types.object_creation_time.deserialize_xml(
                child_created_after
            )
        )
    child_created_before = el.find("CreatedBefore")
    if child_created_before is not None:
        import aws_sdk_s3_control.types.object_creation_time

        out["created_before"] = (
            aws_sdk_s3_control.types.object_creation_time.deserialize_xml(
                child_created_before
            )
        )
    child_object_replication_statuses = el.find("ObjectReplicationStatuses")
    if child_object_replication_statuses is not None:
        import aws_sdk_s3_control.types.replication_status_filter_list

        out["object_replication_statuses"] = (
            aws_sdk_s3_control.types.replication_status_filter_list.deserialize_xml(
                child_object_replication_statuses
            )
        )
    child_key_name_constraint = el.find("KeyNameConstraint")
    if child_key_name_constraint is not None:
        import aws_sdk_s3_control.types.key_name_constraint

        out["key_name_constraint"] = (
            aws_sdk_s3_control.types.key_name_constraint.deserialize_xml(
                child_key_name_constraint
            )
        )
    child_object_size_greater_than_bytes = el.find("ObjectSizeGreaterThanBytes")
    if child_object_size_greater_than_bytes is not None:
        out["object_size_greater_than_bytes"] = int(
            child_object_size_greater_than_bytes.text or ""
        )
    child_object_size_less_than_bytes = el.find("ObjectSizeLessThanBytes")
    if child_object_size_less_than_bytes is not None:
        out["object_size_less_than_bytes"] = int(
            child_object_size_less_than_bytes.text or ""
        )
    child_match_any_storage_class = el.find("MatchAnyStorageClass")
    if child_match_any_storage_class is not None:
        import aws_sdk_s3_control.types.storage_class_list

        out["match_any_storage_class"] = (
            aws_sdk_s3_control.types.storage_class_list.deserialize_xml(
                child_match_any_storage_class
            )
        )
    child_match_any_object_encryption = el.find("MatchAnyObjectEncryption")
    if child_match_any_object_encryption is not None:
        import aws_sdk_s3_control.types.object_encryption_filter_list

        out["match_any_object_encryption"] = (
            aws_sdk_s3_control.types.object_encryption_filter_list.deserialize_xml(
                child_match_any_object_encryption
            )
        )
    return out
