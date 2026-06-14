"""Generated from Smithy shape ``com.amazonaws.storagegateway#Tape``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.double_object
    import aws_sdk_storage_gateway.types.kms_key
    import aws_sdk_storage_gateway.types.pool_id
    import aws_sdk_storage_gateway.types.tape_arn
    import aws_sdk_storage_gateway.types.tape_barcode
    import aws_sdk_storage_gateway.types.tape_size
    import aws_sdk_storage_gateway.types.tape_status
    import aws_sdk_storage_gateway.types.tape_usage
    import aws_sdk_storage_gateway.types.time
    import aws_sdk_storage_gateway.types.vtl_device_arn


class Tape(TypedDict):
    tape_arn: NotRequired["aws_sdk_storage_gateway.types.tape_arn.TapeARN"]
    """<p>The Amazon Resource Name (ARN) of the virtual tape.</p>"""
    tape_barcode: NotRequired["aws_sdk_storage_gateway.types.tape_barcode.TapeBarcode"]
    """<p>The barcode that identifies a specific virtual tape.</p>"""
    tape_created_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The date the virtual tape was created.</p>"""
    tape_size_in_bytes: NotRequired["aws_sdk_storage_gateway.types.tape_size.TapeSize"]
    """<p>The size, in bytes, of the virtual tape capacity.</p>"""
    tape_status: NotRequired["aws_sdk_storage_gateway.types.tape_status.TapeStatus"]
    """<p>The current state of the virtual tape.</p>"""
    vtl_device: NotRequired["aws_sdk_storage_gateway.types.vtl_device_arn.VTLDeviceARN"]
    """<p>The virtual tape library (VTL) device that the virtual tape is associated with.</p>"""
    progress: NotRequired["aws_sdk_storage_gateway.types.double_object.DoubleObject"]
    """<p>For archiving virtual tapes, indicates how much data remains to be uploaded before archiving is complete.</p> <p>Range: 0 (not started) to 100 (complete).</p>"""
    tape_used_in_bytes: NotRequired[
        "aws_sdk_storage_gateway.types.tape_usage.TapeUsage"
    ]
    """<p>The size, in bytes, of data stored on the virtual tape.</p> <note> <p>This value is not available for tapes created prior to May 13, 2015.</p> </note>"""
    kms_key: NotRequired["aws_sdk_storage_gateway.types.kms_key.KMSKey"]
    pool_id: NotRequired["aws_sdk_storage_gateway.types.pool_id.PoolId"]
    """<p>The ID of the pool that contains tapes that will be archived. The tapes in this pool are archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    worm: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>If the tape is archived as write-once-read-many (WORM), this value is <code>true</code>.</p>"""
    retention_start_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The date that the tape is first archived with tape retention lock enabled.</p>"""
    pool_entry_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The date that the tape enters a custom tape pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tape) -> dict:
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
    if "tape_status" in value:
        out["TapeStatus"] = value["tape_status"]
    if "vtl_device" in value:
        out["VTLDevice"] = value["vtl_device"]
    if "progress" in value:
        out["Progress"] = value["progress"]
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


def deserialize_aws_json_1_1(data: dict) -> Tape:
    out: Tape = {}  # type: ignore[typeddict-item]
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
    if "TapeStatus" in data:
        out["tape_status"] = data["TapeStatus"]
    if "VTLDevice" in data:
        out["vtl_device"] = data["VTLDevice"]
    if "Progress" in data:
        out["progress"] = data["Progress"]
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
