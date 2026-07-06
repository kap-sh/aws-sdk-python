"""Generated from Smithy shape ``com.amazonaws.storagegateway#PoolInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.pool_arn
    import aws_sdk_storage_gateway.types.pool_name
    import aws_sdk_storage_gateway.types.pool_status
    import aws_sdk_storage_gateway.types.retention_lock_time_in_days
    import aws_sdk_storage_gateway.types.retention_lock_type
    import aws_sdk_storage_gateway.types.tape_storage_class


class PoolInfo(TypedDict, closed=True):
    pool_arn: NotRequired["aws_sdk_storage_gateway.types.pool_arn.PoolARN"]
    """<p>The Amazon Resource Name (ARN) of the custom tape pool. Use the <a>ListTapePools</a> operation to return a list of custom tape pools for your account and Amazon Web Services Region.</p>"""
    pool_name: NotRequired["aws_sdk_storage_gateway.types.pool_name.PoolName"]
    r"""<p>The name of the custom tape pool. <code>PoolName</code> can use all ASCII characters, except '/' and '\'.</p>"""
    storage_class: NotRequired[
        "aws_sdk_storage_gateway.types.tape_storage_class.TapeStorageClass"
    ]
    """<p>The storage class that is associated with the custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    retention_lock_type: NotRequired[
        "aws_sdk_storage_gateway.types.retention_lock_type.RetentionLockType"
    ]
    """<p>Tape retention lock type, which can be configured in two modes. When configured in governance mode, Amazon Web Services accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root Amazon Web Services account.</p>"""
    retention_lock_time_in_days: NotRequired[
        "aws_sdk_storage_gateway.types.retention_lock_time_in_days.RetentionLockTimeInDays"
    ]
    """<p>Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days).</p>"""
    pool_status: NotRequired["aws_sdk_storage_gateway.types.pool_status.PoolStatus"]
    """<p>Status of the custom tape pool. Pool can be <code>ACTIVE</code> or <code>DELETED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PoolInfo) -> dict:
    out: dict = {}
    if "pool_arn" in value:
        out["PoolARN"] = value["pool_arn"]
    if "pool_name" in value:
        out["PoolName"] = value["pool_name"]
    if "storage_class" in value:
        import aws_sdk_storage_gateway.types.tape_storage_class

        out["StorageClass"] = (
            aws_sdk_storage_gateway.types.tape_storage_class.serialize_aws_json_1_1(
                value["storage_class"]
            )
        )
    if "retention_lock_type" in value:
        import aws_sdk_storage_gateway.types.retention_lock_type

        out["RetentionLockType"] = (
            aws_sdk_storage_gateway.types.retention_lock_type.serialize_aws_json_1_1(
                value["retention_lock_type"]
            )
        )
    if "retention_lock_time_in_days" in value:
        out["RetentionLockTimeInDays"] = value["retention_lock_time_in_days"]
    if "pool_status" in value:
        import aws_sdk_storage_gateway.types.pool_status

        out["PoolStatus"] = (
            aws_sdk_storage_gateway.types.pool_status.serialize_aws_json_1_1(
                value["pool_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PoolInfo:
    out: PoolInfo = {}  # type: ignore[typeddict-item]
    if "PoolARN" in data:
        out["pool_arn"] = data["PoolARN"]
    if "PoolName" in data:
        out["pool_name"] = data["PoolName"]
    if "StorageClass" in data:
        import aws_sdk_storage_gateway.types.tape_storage_class

        out["storage_class"] = (
            aws_sdk_storage_gateway.types.tape_storage_class.deserialize_aws_json_1_1(
                data["StorageClass"]
            )
        )
    if "RetentionLockType" in data:
        import aws_sdk_storage_gateway.types.retention_lock_type

        out["retention_lock_type"] = (
            aws_sdk_storage_gateway.types.retention_lock_type.deserialize_aws_json_1_1(
                data["RetentionLockType"]
            )
        )
    if "RetentionLockTimeInDays" in data:
        out["retention_lock_time_in_days"] = data["RetentionLockTimeInDays"]
    if "PoolStatus" in data:
        import aws_sdk_storage_gateway.types.pool_status

        out["pool_status"] = (
            aws_sdk_storage_gateway.types.pool_status.deserialize_aws_json_1_1(
                data["PoolStatus"]
            )
        )
    return out
