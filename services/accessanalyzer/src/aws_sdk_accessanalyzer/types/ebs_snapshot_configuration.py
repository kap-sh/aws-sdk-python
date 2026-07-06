"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#EbsSnapshotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.ebs_group_list
    import aws_sdk_accessanalyzer.types.ebs_snapshot_data_encryption_key_id
    import aws_sdk_accessanalyzer.types.ebs_user_id_list


class EbsSnapshotConfiguration(TypedDict, closed=True):
    user_ids: NotRequired["aws_sdk_accessanalyzer.types.ebs_user_id_list.EbsUserIdList"]
    """<p>The IDs of the Amazon Web Services accounts that have access to the Amazon EBS volume snapshot.</p> <ul> <li> <p>If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the <code>userIds</code>, then the access preview uses the existing shared <code>userIds</code> for the snapshot.</p> </li> <li> <p>If the access preview is for a new resource and you do not specify the <code>userIds</code>, then the access preview considers the snapshot without any <code>userIds</code>.</p> </li> <li> <p>To propose deletion of existing shared <code>accountIds</code>, you can specify an empty list for <code>userIds</code>.</p> </li> </ul>"""
    groups: NotRequired["aws_sdk_accessanalyzer.types.ebs_group_list.EbsGroupList"]
    """<p>The groups that have access to the Amazon EBS volume snapshot. If the value <code>all</code> is specified, then the Amazon EBS volume snapshot is public.</p> <ul> <li> <p>If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the <code>groups</code>, then the access preview uses the existing shared <code>groups</code> for the snapshot.</p> </li> <li> <p>If the access preview is for a new resource and you do not specify the <code>groups</code>, then the access preview considers the snapshot without any <code>groups</code>.</p> </li> <li> <p>To propose deletion of existing shared <code>groups</code>, you can specify an empty list for <code>groups</code>.</p> </li> </ul>"""
    kms_key_id: NotRequired[
        "aws_sdk_accessanalyzer.types.ebs_snapshot_data_encryption_key_id.EbsSnapshotDataEncryptionKeyId"
    ]
    """<p>The KMS key identifier for an encrypted Amazon EBS volume snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <ul> <li> <p>If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the <code>kmsKeyId</code>, or you specify an empty string, then the access preview uses the existing <code>kmsKeyId</code> of the snapshot.</p> </li> <li> <p>If the access preview is for a new resource and you do not specify the <code>kmsKeyId</code>, the access preview considers the snapshot as unencrypted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsSnapshotConfiguration) -> dict:
    out: dict = {}
    if "user_ids" in value:
        import aws_sdk_accessanalyzer.types.ebs_user_id_list

        out["userIds"] = aws_sdk_accessanalyzer.types.ebs_user_id_list.serialize_json(
            value["user_ids"]
        )
    if "groups" in value:
        import aws_sdk_accessanalyzer.types.ebs_group_list

        out["groups"] = aws_sdk_accessanalyzer.types.ebs_group_list.serialize_json(
            value["groups"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> EbsSnapshotConfiguration:
    out: EbsSnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if "userIds" in data:
        import aws_sdk_accessanalyzer.types.ebs_user_id_list

        out["user_ids"] = (
            aws_sdk_accessanalyzer.types.ebs_user_id_list.deserialize_json(
                data["userIds"]
            )
        )
    if "groups" in data:
        import aws_sdk_accessanalyzer.types.ebs_group_list

        out["groups"] = aws_sdk_accessanalyzer.types.ebs_group_list.deserialize_json(
            data["groups"]
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
