"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.pool_id
    import aws_sdk_storage_gateway.types.tape_arn
    import aws_sdk_storage_gateway.types.tape_barcode
    import aws_sdk_storage_gateway.types.tape_size
    import aws_sdk_storage_gateway.types.tape_status
    import aws_sdk_storage_gateway.types.time


class TapeInfo(TypedDict):
    tape_arn: NotRequired["aws_sdk_storage_gateway.types.tape_arn.TapeARN"]
    """<p>The Amazon Resource Name (ARN) of a virtual tape.</p>"""
    tape_barcode: NotRequired["aws_sdk_storage_gateway.types.tape_barcode.TapeBarcode"]
    """<p>The barcode that identifies a specific virtual tape.</p>"""
    tape_size_in_bytes: NotRequired["aws_sdk_storage_gateway.types.tape_size.TapeSize"]
    """<p>The size, in bytes, of a virtual tape.</p>"""
    tape_status: NotRequired["aws_sdk_storage_gateway.types.tape_status.TapeStatus"]
    """<p>The status of the tape.</p>"""
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    pool_id: NotRequired["aws_sdk_storage_gateway.types.pool_id.PoolId"]
    """<p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    retention_start_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The date that the tape became subject to tape retention lock.</p>"""
    pool_entry_date: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The date that the tape entered the custom tape pool with tape retention lock enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeInfo) -> dict:
    out: dict = {}
    if "tape_arn" in value:
        out["TapeARN"] = value["tape_arn"]
    if "tape_barcode" in value:
        out["TapeBarcode"] = value["tape_barcode"]
    if "tape_size_in_bytes" in value:
        out["TapeSizeInBytes"] = value["tape_size_in_bytes"]
    if "tape_status" in value:
        out["TapeStatus"] = value["tape_status"]
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
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


def deserialize_aws_json_1_1(data: dict) -> TapeInfo:
    out: TapeInfo = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    if "TapeBarcode" in data:
        out["tape_barcode"] = data["TapeBarcode"]
    if "TapeSizeInBytes" in data:
        out["tape_size_in_bytes"] = data["TapeSizeInBytes"]
    if "TapeStatus" in data:
        out["tape_status"] = data["TapeStatus"]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
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
