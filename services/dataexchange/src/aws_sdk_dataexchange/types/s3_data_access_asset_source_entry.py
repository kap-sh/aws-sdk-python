"""Generated from Smithy shape ``com.amazonaws.dataexchange#S3DataAccessAssetSourceEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.list_of__string
    import aws_sdk_dataexchange.types.list_of_kms_keys_to_grant


class S3DataAccessAssetSourceEntry(TypedDict, closed=True):
    bucket: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket used for hosting shared data in the Amazon S3 data access.</p>"""
    key_prefixes: NotRequired[
        "aws_sdk_dataexchange.types.list_of__string.ListOf__string"
    ]
    """<p>Organizes Amazon S3 asset key prefixes stored in an Amazon S3 bucket.</p>"""
    keys: NotRequired["aws_sdk_dataexchange.types.list_of__string.ListOf__string"]
    """<p>The keys used to create the Amazon S3 data access.</p>"""
    kms_keys_to_grant: NotRequired[
        "aws_sdk_dataexchange.types.list_of_kms_keys_to_grant.ListOfKmsKeysToGrant"
    ]
    """<p>List of AWS KMS CMKs (Key Management System Customer Managed Keys) and ARNs used to encrypt S3 objects being shared in this S3 Data Access asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DataAccessAssetSourceEntry) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "key_prefixes" in value:
        import aws_sdk_dataexchange.types.list_of__string

        out["KeyPrefixes"] = aws_sdk_dataexchange.types.list_of__string.serialize_json(
            value["key_prefixes"]
        )
    if "keys" in value:
        import aws_sdk_dataexchange.types.list_of__string

        out["Keys"] = aws_sdk_dataexchange.types.list_of__string.serialize_json(
            value["keys"]
        )
    if "kms_keys_to_grant" in value:
        import aws_sdk_dataexchange.types.list_of_kms_keys_to_grant

        out["KmsKeysToGrant"] = (
            aws_sdk_dataexchange.types.list_of_kms_keys_to_grant.serialize_json(
                value["kms_keys_to_grant"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3DataAccessAssetSourceEntry:
    out: S3DataAccessAssetSourceEntry = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("S3DataAccessAssetSourceEntry.bucket required")
    if "KeyPrefixes" in data:
        import aws_sdk_dataexchange.types.list_of__string

        out["key_prefixes"] = (
            aws_sdk_dataexchange.types.list_of__string.deserialize_json(
                data["KeyPrefixes"]
            )
        )
    if "Keys" in data:
        import aws_sdk_dataexchange.types.list_of__string

        out["keys"] = aws_sdk_dataexchange.types.list_of__string.deserialize_json(
            data["Keys"]
        )
    if "KmsKeysToGrant" in data:
        import aws_sdk_dataexchange.types.list_of_kms_keys_to_grant

        out["kms_keys_to_grant"] = (
            aws_sdk_dataexchange.types.list_of_kms_keys_to_grant.deserialize_json(
                data["KmsKeysToGrant"]
            )
        )
    return out
