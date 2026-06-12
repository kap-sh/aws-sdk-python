"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateTapesInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.client_token
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.kms_key
    import aws_sdk_storage_gateway.types.num_tapes_to_create
    import aws_sdk_storage_gateway.types.pool_id
    import aws_sdk_storage_gateway.types.tags
    import aws_sdk_storage_gateway.types.tape_barcode_prefix
    import aws_sdk_storage_gateway.types.tape_size


class CreateTapesInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tapes with. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    tape_size_in_bytes: "aws_sdk_storage_gateway.types.tape_size.TapeSize"
    """<p>The size, in bytes, of the virtual tapes that you want to create.</p> <note> <p>The size must be aligned by gigabyte (1024*1024*1024 bytes).</p> </note>"""
    client_token: "aws_sdk_storage_gateway.types.client_token.ClientToken"
    """<p>A unique identifier that you use to retry a request. If you retry a request, use the same <code>ClientToken</code> you specified in the initial request.</p> <note> <p>Using the same <code>ClientToken</code> prevents creating the tape multiple times.</p> </note>"""
    num_tapes_to_create: (
        "aws_sdk_storage_gateway.types.num_tapes_to_create.NumTapesToCreate"
    )
    """<p>The number of virtual tapes that you want to create.</p>"""
    tape_barcode_prefix: (
        "aws_sdk_storage_gateway.types.tape_barcode_prefix.TapeBarcodePrefix"
    )
    """<p>A prefix that you append to the barcode of the virtual tape you are creating. This prefix makes the barcode unique.</p> <note> <p>The prefix must be 1-4 characters in length and must be one of the uppercase letters from A to Z.</p> </note>"""
    kms_encrypted: NotRequired["aws_sdk_storage_gateway.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    kms_key: NotRequired["aws_sdk_storage_gateway.types.kms_key.KMSKey"]
    """<p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>"""
    pool_id: NotRequired["aws_sdk_storage_gateway.types.pool_id.PoolId"]
    """<p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    worm: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>Set to <code>TRUE</code> if the tape you are creating is to be configured as a write-once-read-many (WORM) tape.</p>"""
    tags: NotRequired["aws_sdk_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that can be assigned to a virtual tape. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTapesInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["TapeSizeInBytes"] = value["tape_size_in_bytes"]
    out["ClientToken"] = value["client_token"]
    out["NumTapesToCreate"] = value["num_tapes_to_create"]
    out["TapeBarcodePrefix"] = value["tape_barcode_prefix"]
    if "kms_encrypted" in value:
        out["KMSEncrypted"] = value["kms_encrypted"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    out["Worm"] = value.get("worm", False)
    if "tags" in value:
        import aws_sdk_storage_gateway.types.tags

        out["Tags"] = aws_sdk_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTapesInput:
    out: CreateTapesInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("CreateTapesInput.gateway_arn required")
    if "TapeSizeInBytes" in data:
        out["tape_size_in_bytes"] = data["TapeSizeInBytes"]
    else:
        raise DeserializationError("CreateTapesInput.tape_size_in_bytes required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateTapesInput.client_token required")
    if "NumTapesToCreate" in data:
        out["num_tapes_to_create"] = data["NumTapesToCreate"]
    else:
        raise DeserializationError("CreateTapesInput.num_tapes_to_create required")
    if "TapeBarcodePrefix" in data:
        out["tape_barcode_prefix"] = data["TapeBarcodePrefix"]
    else:
        raise DeserializationError("CreateTapesInput.tape_barcode_prefix required")
    if "KMSEncrypted" in data:
        out["kms_encrypted"] = data["KMSEncrypted"]
    if "KMSKey" in data:
        out["kms_key"] = data["KMSKey"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "Worm" in data:
        out["worm"] = data["Worm"]
    else:
        out["worm"] = False
    if "Tags" in data:
        import aws_sdk_storage_gateway.types.tags

        out["tags"] = aws_sdk_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
