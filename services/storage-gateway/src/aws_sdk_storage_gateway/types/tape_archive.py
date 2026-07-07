"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeArchive``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.kms_key
    import aws_sdk_storage_gateway.types.pool_id
    import aws_sdk_storage_gateway.types.tape_archive_status
    import aws_sdk_storage_gateway.types.tape_arn
    import aws_sdk_storage_gateway.types.tape_barcode
    import aws_sdk_storage_gateway.types.tape_size
    import aws_sdk_storage_gateway.types.tape_usage
    import aws_sdk_storage_gateway.types.time


class TapeArchive(TypedDict, closed=True):
    tape_arn: NotRequired["aws_sdk_storage_gateway.types.tape_arn.TapeARN"]
    """<p>The Amazon Resource Name (ARN) of an archived virtual tape.</p>"""
    tape_barcode: NotRequired["aws_sdk_storage_gateway.types.tape_barcode.TapeBarcode"]
    """<p>The barcode that identifies the archived virtual tape.</p>"""
    tape_created_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The date the virtual tape was created.</p>"""
    tape_size_in_bytes: NotRequired["aws_sdk_storage_gateway.types.tape_size.TapeSize"]
    """<p>The size, in bytes, of the archived virtual tape.</p>"""
    completion_time: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The time that the archiving of the virtual tape was completed.</p> <p>The default timestamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.</p>"""
    retrieved_to: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    """<p>The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being retrieved to.</p> <p>The virtual tape is retrieved from the virtual tape shelf (VTS).</p>"""
    tape_status: NotRequired[
        "aws_sdk_storage_gateway.types.tape_archive_status.TapeArchiveStatus"
    ]
    """<p>The current state of the archived virtual tape.</p>"""
    tape_used_in_bytes: NotRequired[
        "aws_sdk_storage_gateway.types.tape_usage.TapeUsage"
    ]
    """<p>The size, in bytes, of data stored on the virtual tape.</p> <note> <p>This value is not available for tapes created prior to May 13, 2015.</p> </note>"""
    kms_key: NotRequired["aws_sdk_storage_gateway.types.kms_key.KMSKey"]
    pool_id: NotRequired["aws_sdk_storage_gateway.types.pool_id.PoolId"]
    """<p>The ID of the pool that was used to archive the tape. The tapes in this pool are archived in the S3 storage class that is associated with the pool.</p>"""
    worm: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>Set to <code>true</code> if the archived tape is stored as write-once-read-many (WORM).</p>"""
    retention_start_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>If the archived tape is subject to tape retention lock, the date that the archived tape started being retained.</p>"""
    pool_entry_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The time that the tape entered the custom tape pool.</p> <p>The default timestamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeArchive) -> dict:
    out: dict = {}
    if "tape_arn" in value:
        out["TapeARN"] = value["tape_arn"]
    if "tape_barcode" in value:
        out["TapeBarcode"] = value["tape_barcode"]
    if "tape_created_date" in value:
        import aws_sdk_storage_gateway.types.time

        out["TapeCreatedDate"] = (
            aws_sdk_storage_gateway.types.time.serialize_aws_json_1_1(
                value["tape_created_date"]
            )
        )
    if "tape_size_in_bytes" in value:
        out["TapeSizeInBytes"] = value["tape_size_in_bytes"]
    if "completion_time" in value:
        import aws_sdk_storage_gateway.types.time

        out["CompletionTime"] = (
            aws_sdk_storage_gateway.types.time.serialize_aws_json_1_1(
                value["completion_time"]
            )
        )
    if "retrieved_to" in value:
        out["RetrievedTo"] = value["retrieved_to"]
    if "tape_status" in value:
        out["TapeStatus"] = value["tape_status"]
    if "tape_used_in_bytes" in value:
        out["TapeUsedInBytes"] = value["tape_used_in_bytes"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    out["Worm"] = value.get("worm", False)
    if "retention_start_date" in value:
        import aws_sdk_storage_gateway.types.time

        out["RetentionStartDate"] = (
            aws_sdk_storage_gateway.types.time.serialize_aws_json_1_1(
                value["retention_start_date"]
            )
        )
    if "pool_entry_date" in value:
        import aws_sdk_storage_gateway.types.time

        out["PoolEntryDate"] = (
            aws_sdk_storage_gateway.types.time.serialize_aws_json_1_1(
                value["pool_entry_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TapeArchive:
    out: TapeArchive = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    if "TapeBarcode" in data:
        out["tape_barcode"] = data["TapeBarcode"]
    if "TapeCreatedDate" in data:
        import aws_sdk_storage_gateway.types.time

        out["tape_created_date"] = (
            aws_sdk_storage_gateway.types.time.deserialize_aws_json_1_1(
                data["TapeCreatedDate"]
            )
        )
    if "TapeSizeInBytes" in data:
        out["tape_size_in_bytes"] = data["TapeSizeInBytes"]
    if "CompletionTime" in data:
        import aws_sdk_storage_gateway.types.time

        out["completion_time"] = (
            aws_sdk_storage_gateway.types.time.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if "RetrievedTo" in data:
        out["retrieved_to"] = data["RetrievedTo"]
    if "TapeStatus" in data:
        out["tape_status"] = data["TapeStatus"]
    if "TapeUsedInBytes" in data:
        out["tape_used_in_bytes"] = data["TapeUsedInBytes"]
    if "KMSKey" in data:
        out["kms_key"] = data["KMSKey"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "Worm" in data:
        out["worm"] = data["Worm"]
    else:
        out["worm"] = False
    if "RetentionStartDate" in data:
        import aws_sdk_storage_gateway.types.time

        out["retention_start_date"] = (
            aws_sdk_storage_gateway.types.time.deserialize_aws_json_1_1(
                data["RetentionStartDate"]
            )
        )
    if "PoolEntryDate" in data:
        import aws_sdk_storage_gateway.types.time

        out["pool_entry_date"] = (
            aws_sdk_storage_gateway.types.time.deserialize_aws_json_1_1(
                data["PoolEntryDate"]
            )
        )
    return out
