"""Generated from Smithy shape ``com.amazonaws.s3control#JobOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.lambda_invoke_operation
    import aws_sdk_s3_control.types.s3_compute_object_checksum_operation
    import aws_sdk_s3_control.types.s3_copy_object_operation
    import aws_sdk_s3_control.types.s3_delete_object_tagging_operation
    import aws_sdk_s3_control.types.s3_initiate_restore_object_operation
    import aws_sdk_s3_control.types.s3_replicate_object_operation
    import aws_sdk_s3_control.types.s3_set_object_acl_operation
    import aws_sdk_s3_control.types.s3_set_object_legal_hold_operation
    import aws_sdk_s3_control.types.s3_set_object_retention_operation
    import aws_sdk_s3_control.types.s3_set_object_tagging_operation
    import aws_sdk_s3_control.types.s3_update_object_encryption_operation


class JobOperation(TypedDict, closed=True):
    lambda_invoke: NotRequired[
        "aws_sdk_s3_control.types.lambda_invoke_operation.LambdaInvokeOperation"
    ]
    """<p>Directs the specified job to invoke an Lambda function on every object in the manifest.</p>"""
    s3_put_object_copy: NotRequired[
        "aws_sdk_s3_control.types.s3_copy_object_operation.S3CopyObjectOperation"
    ]
    """<p>Directs the specified job to run a PUT Copy object call on every object in the manifest.</p>"""
    s3_put_object_acl: NotRequired[
        "aws_sdk_s3_control.types.s3_set_object_acl_operation.S3SetObjectAclOperation"
    ]
    """<p>Directs the specified job to run a <code>PutObjectAcl</code> call on every object in the manifest.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    s3_put_object_tagging: NotRequired[
        "aws_sdk_s3_control.types.s3_set_object_tagging_operation.S3SetObjectTaggingOperation"
    ]
    """<p>Directs the specified job to run a PUT Object tagging call on every object in the manifest.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    s3_delete_object_tagging: NotRequired[
        "aws_sdk_s3_control.types.s3_delete_object_tagging_operation.S3DeleteObjectTaggingOperation"
    ]
    """<p>Directs the specified job to execute a DELETE Object tagging call on every object in the manifest.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    s3_initiate_restore_object: NotRequired[
        "aws_sdk_s3_control.types.s3_initiate_restore_object_operation.S3InitiateRestoreObjectOperation"
    ]
    """<p>Directs the specified job to initiate restore requests for every archived object in the manifest.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    s3_put_object_legal_hold: NotRequired[
        "aws_sdk_s3_control.types.s3_set_object_legal_hold_operation.S3SetObjectLegalHoldOperation"
    ]
    s3_put_object_retention: NotRequired[
        "aws_sdk_s3_control.types.s3_set_object_retention_operation.S3SetObjectRetentionOperation"
    ]
    s3_replicate_object: NotRequired[
        "aws_sdk_s3_control.types.s3_replicate_object_operation.S3ReplicateObjectOperation"
    ]
    """<p>Directs the specified job to invoke <code>ReplicateObject</code> on every object in the job's manifest.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    s3_compute_object_checksum: NotRequired[
        "aws_sdk_s3_control.types.s3_compute_object_checksum_operation.S3ComputeObjectChecksumOperation"
    ]
    """<p>Directs the specified job to compute checksum values for every object in the manifest.</p>"""
    s3_update_object_encryption: NotRequired[
        "aws_sdk_s3_control.types.s3_update_object_encryption_operation.S3UpdateObjectEncryptionOperation"
    ]
    """<p>Updates the server-side encryption type of an existing encrypted object in a general purpose bucket. You can use the <code>UpdateObjectEncryption</code> operation to change encrypted objects from server-side encryption with Amazon S3 managed keys (SSE-S3) to server-side encryption with Key Management Service (KMS) keys (SSE-KMS), or to apply S3 Bucket Keys. You can also use the <code>UpdateObjectEncryption</code> operation to change the customer-managed KMS key used to encrypt your data so that you can comply with custom key-rotation standards.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobOperation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "lambda_invoke" in value:
        import aws_sdk_s3_control.types.lambda_invoke_operation

        aws_sdk_s3_control.types.lambda_invoke_operation.serialize_xml(
            value["lambda_invoke"], el, "LambdaInvoke"
        )
    if "s3_put_object_copy" in value:
        import aws_sdk_s3_control.types.s3_copy_object_operation

        aws_sdk_s3_control.types.s3_copy_object_operation.serialize_xml(
            value["s3_put_object_copy"], el, "S3PutObjectCopy"
        )
    if "s3_put_object_acl" in value:
        import aws_sdk_s3_control.types.s3_set_object_acl_operation

        aws_sdk_s3_control.types.s3_set_object_acl_operation.serialize_xml(
            value["s3_put_object_acl"], el, "S3PutObjectAcl"
        )
    if "s3_put_object_tagging" in value:
        import aws_sdk_s3_control.types.s3_set_object_tagging_operation

        aws_sdk_s3_control.types.s3_set_object_tagging_operation.serialize_xml(
            value["s3_put_object_tagging"], el, "S3PutObjectTagging"
        )
    if "s3_delete_object_tagging" in value:
        import aws_sdk_s3_control.types.s3_delete_object_tagging_operation

        aws_sdk_s3_control.types.s3_delete_object_tagging_operation.serialize_xml(
            value["s3_delete_object_tagging"], el, "S3DeleteObjectTagging"
        )
    if "s3_initiate_restore_object" in value:
        import aws_sdk_s3_control.types.s3_initiate_restore_object_operation

        aws_sdk_s3_control.types.s3_initiate_restore_object_operation.serialize_xml(
            value["s3_initiate_restore_object"], el, "S3InitiateRestoreObject"
        )
    if "s3_put_object_legal_hold" in value:
        import aws_sdk_s3_control.types.s3_set_object_legal_hold_operation

        aws_sdk_s3_control.types.s3_set_object_legal_hold_operation.serialize_xml(
            value["s3_put_object_legal_hold"], el, "S3PutObjectLegalHold"
        )
    if "s3_put_object_retention" in value:
        import aws_sdk_s3_control.types.s3_set_object_retention_operation

        aws_sdk_s3_control.types.s3_set_object_retention_operation.serialize_xml(
            value["s3_put_object_retention"], el, "S3PutObjectRetention"
        )
    if "s3_replicate_object" in value:
        import aws_sdk_s3_control.types.s3_replicate_object_operation

        aws_sdk_s3_control.types.s3_replicate_object_operation.serialize_xml(
            value["s3_replicate_object"], el, "S3ReplicateObject"
        )
    if "s3_compute_object_checksum" in value:
        import aws_sdk_s3_control.types.s3_compute_object_checksum_operation

        aws_sdk_s3_control.types.s3_compute_object_checksum_operation.serialize_xml(
            value["s3_compute_object_checksum"], el, "S3ComputeObjectChecksum"
        )
    if "s3_update_object_encryption" in value:
        import aws_sdk_s3_control.types.s3_update_object_encryption_operation

        aws_sdk_s3_control.types.s3_update_object_encryption_operation.serialize_xml(
            value["s3_update_object_encryption"], el, "S3UpdateObjectEncryption"
        )


def deserialize_xml(el: Element) -> JobOperation:
    out: JobOperation = {}  # type: ignore[typeddict-item]
    child_lambda_invoke = el.find("LambdaInvoke")
    if child_lambda_invoke is not None:
        import aws_sdk_s3_control.types.lambda_invoke_operation

        out["lambda_invoke"] = (
            aws_sdk_s3_control.types.lambda_invoke_operation.deserialize_xml(
                child_lambda_invoke
            )
        )
    child_s3_put_object_copy = el.find("S3PutObjectCopy")
    if child_s3_put_object_copy is not None:
        import aws_sdk_s3_control.types.s3_copy_object_operation

        out["s3_put_object_copy"] = (
            aws_sdk_s3_control.types.s3_copy_object_operation.deserialize_xml(
                child_s3_put_object_copy
            )
        )
    child_s3_put_object_acl = el.find("S3PutObjectAcl")
    if child_s3_put_object_acl is not None:
        import aws_sdk_s3_control.types.s3_set_object_acl_operation

        out["s3_put_object_acl"] = (
            aws_sdk_s3_control.types.s3_set_object_acl_operation.deserialize_xml(
                child_s3_put_object_acl
            )
        )
    child_s3_put_object_tagging = el.find("S3PutObjectTagging")
    if child_s3_put_object_tagging is not None:
        import aws_sdk_s3_control.types.s3_set_object_tagging_operation

        out["s3_put_object_tagging"] = (
            aws_sdk_s3_control.types.s3_set_object_tagging_operation.deserialize_xml(
                child_s3_put_object_tagging
            )
        )
    child_s3_delete_object_tagging = el.find("S3DeleteObjectTagging")
    if child_s3_delete_object_tagging is not None:
        import aws_sdk_s3_control.types.s3_delete_object_tagging_operation

        out["s3_delete_object_tagging"] = (
            aws_sdk_s3_control.types.s3_delete_object_tagging_operation.deserialize_xml(
                child_s3_delete_object_tagging
            )
        )
    child_s3_initiate_restore_object = el.find("S3InitiateRestoreObject")
    if child_s3_initiate_restore_object is not None:
        import aws_sdk_s3_control.types.s3_initiate_restore_object_operation

        out["s3_initiate_restore_object"] = (
            aws_sdk_s3_control.types.s3_initiate_restore_object_operation.deserialize_xml(
                child_s3_initiate_restore_object
            )
        )
    child_s3_put_object_legal_hold = el.find("S3PutObjectLegalHold")
    if child_s3_put_object_legal_hold is not None:
        import aws_sdk_s3_control.types.s3_set_object_legal_hold_operation

        out["s3_put_object_legal_hold"] = (
            aws_sdk_s3_control.types.s3_set_object_legal_hold_operation.deserialize_xml(
                child_s3_put_object_legal_hold
            )
        )
    child_s3_put_object_retention = el.find("S3PutObjectRetention")
    if child_s3_put_object_retention is not None:
        import aws_sdk_s3_control.types.s3_set_object_retention_operation

        out["s3_put_object_retention"] = (
            aws_sdk_s3_control.types.s3_set_object_retention_operation.deserialize_xml(
                child_s3_put_object_retention
            )
        )
    child_s3_replicate_object = el.find("S3ReplicateObject")
    if child_s3_replicate_object is not None:
        import aws_sdk_s3_control.types.s3_replicate_object_operation

        out["s3_replicate_object"] = (
            aws_sdk_s3_control.types.s3_replicate_object_operation.deserialize_xml(
                child_s3_replicate_object
            )
        )
    child_s3_compute_object_checksum = el.find("S3ComputeObjectChecksum")
    if child_s3_compute_object_checksum is not None:
        import aws_sdk_s3_control.types.s3_compute_object_checksum_operation

        out["s3_compute_object_checksum"] = (
            aws_sdk_s3_control.types.s3_compute_object_checksum_operation.deserialize_xml(
                child_s3_compute_object_checksum
            )
        )
    child_s3_update_object_encryption = el.find("S3UpdateObjectEncryption")
    if child_s3_update_object_encryption is not None:
        import aws_sdk_s3_control.types.s3_update_object_encryption_operation

        out["s3_update_object_encryption"] = (
            aws_sdk_s3_control.types.s3_update_object_encryption_operation.deserialize_xml(
                child_s3_update_object_encryption
            )
        )
    return out
