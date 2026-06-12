"""Generated from Smithy shape ``com.amazonaws.docdb#CopyDBClusterSnapshotMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.string
    import aws_sdk_docdb.types.tag_list


class CopyDBClusterSnapshotMessage(TypedDict):
    source_db_cluster_snapshot_identifier: NotRequired[
        "aws_sdk_docdb.types.string.String"
    ]
    """<p>The identifier of the cluster snapshot to copy. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid cluster snapshot in the <i>available</i> state.</p> </li> <li> <p>If the source cluster snapshot is in the same Amazon Web Services Region as the copy, specify a valid snapshot identifier.</p> </li> <li> <p>If the source cluster snapshot is in a different Amazon Web Services Region or owned by another Amazon Web Services account, specify the snapshot ARN.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot1</code> </p>"""
    target_db_cluster_snapshot_identifier: NotRequired[
        "aws_sdk_docdb.types.string.String"
    ]
    """<p>The identifier of the new cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens. </p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens. </p> </li> </ul> <p>Example: <code>my-cluster-snapshot2</code> </p>"""
    kms_key_id: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The KMS key ID for an encrypted cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key. </p> <p>If you copy an encrypted cluster snapshot from your Amazon Web Services account, you can specify a value for <code>KmsKeyId</code> to encrypt the copy with a new KMS encryption key. If you don't specify a value for <code>KmsKeyId</code>, then the copy of the cluster snapshot is encrypted with the same KMS key as the source cluster snapshot.</p> <p>If you copy an encrypted cluster snapshot that is shared from another Amazon Web Services account, then you must specify a value for <code>KmsKeyId</code>.</p> <p>To copy an encrypted cluster snapshot to another Amazon Web Services Region, set <code>KmsKeyId</code> to the KMS key ID that you want to use to encrypt the copy of the cluster snapshot in the destination Region. KMS encryption keys are specific to the Amazon Web Services Region that they are created in, and you can't use encryption keys from one Amazon Web Services Region in another Amazon Web Services Region.</p> <p>If you copy an unencrypted cluster snapshot and specify a value for the <code>KmsKeyId</code> parameter, an error is returned.</p>"""
    pre_signed_url: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The URL that contains a Signature Version 4 signed request for the<code>CopyDBClusterSnapshot</code> API action in the Amazon Web Services Region that contains the source cluster snapshot to copy. You must use the <code>PreSignedUrl</code> parameter when copying a cluster snapshot from another Amazon Web Services Region.</p> <p>If you are using an Amazon Web Services SDK tool or the CLI, you can specify <code>SourceRegion</code> (or <code>--source-region</code> for the CLI) instead of specifying <code>PreSignedUrl</code> manually. Specifying <code>SourceRegion</code> autogenerates a pre-signed URL that is a valid request for the operation that can be executed in the source Amazon Web Services Region.</p> <p>The presigned URL must be a valid request for the <code>CopyDBClusterSnapshot</code> API action that can be executed in the source Amazon Web Services Region that contains the cluster snapshot to be copied. The presigned URL request must contain the following parameter values:</p> <ul> <li> <p> <code>SourceRegion</code> - The ID of the region that contains the snapshot to be copied.</p> </li> <li> <p> <code>SourceDBClusterSnapshotIdentifier</code> - The identifier for the the encrypted cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted cluster snapshot from the us-east-1 Amazon Web Services Region, then your <code>SourceDBClusterSnapshotIdentifier</code> looks something like the following: <code>arn:aws:rds:us-east-1:12345678012:sample-cluster:sample-cluster-snapshot</code>.</p> </li> <li> <p> <code>TargetDBClusterSnapshotIdentifier</code> - The identifier for the new cluster snapshot to be created. This parameter isn't case sensitive.</p> </li> </ul>"""
    copy_tags: NotRequired["aws_sdk_docdb.types.boolean_optional.BooleanOptional"]
    """<p>Set to <code>true</code> to copy all tags from the source cluster snapshot to the target cluster snapshot, and otherwise <code>false</code>. The default is <code>false</code>.</p>"""
    tags: NotRequired["aws_sdk_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the cluster snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyDBClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.SourceDBClusterSnapshotIdentifier",
                str(value["source_db_cluster_snapshot_identifier"]),
            )
        )
    if "target_db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.TargetDBClusterSnapshotIdentifier",
                str(value["target_db_cluster_snapshot_identifier"]),
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "pre_signed_url" in value:
        pairs.append((f"{prefix}.PreSignedUrl", str(value["pre_signed_url"])))
    if "copy_tags" in value:
        pairs.append((f"{prefix}.CopyTags", "true" if value["copy_tags"] else "false"))
    if "tags" in value:
        import aws_sdk_docdb.types.tag_list

        aws_sdk_docdb.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CopyDBClusterSnapshotMessage:
    out: CopyDBClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_source_db_cluster_snapshot_identifier = el.find(
        "SourceDBClusterSnapshotIdentifier"
    )
    if child_source_db_cluster_snapshot_identifier is not None:
        out["source_db_cluster_snapshot_identifier"] = str(
            child_source_db_cluster_snapshot_identifier.text or ""
        )
    child_target_db_cluster_snapshot_identifier = el.find(
        "TargetDBClusterSnapshotIdentifier"
    )
    if child_target_db_cluster_snapshot_identifier is not None:
        out["target_db_cluster_snapshot_identifier"] = str(
            child_target_db_cluster_snapshot_identifier.text or ""
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_pre_signed_url = el.find("PreSignedUrl")
    if child_pre_signed_url is not None:
        out["pre_signed_url"] = str(child_pre_signed_url.text or "")
    child_copy_tags = el.find("CopyTags")
    if child_copy_tags is not None:
        out["copy_tags"] = (child_copy_tags.text or "").lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_docdb.types.tag_list

        out["tags"] = aws_sdk_docdb.types.tag_list.deserialize_query(child_tags)
    return out
