"""Generated from Smithy shape ``com.amazonaws.dataexchange#S3DataAccessAsset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.list_of__string
    import aws_sdk_dataexchange.types.list_of_kms_keys_to_grant


class S3DataAccessAsset(TypedDict):
    bucket: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket hosting data to be shared in the S3 data access.</p>"""
    key_prefixes: NotRequired[
        "aws_sdk_dataexchange.types.list_of__string.ListOf__string"
    ]
    """<p>The Amazon S3 bucket used for hosting shared data in the Amazon S3 data access.</p>"""
    keys: NotRequired["aws_sdk_dataexchange.types.list_of__string.ListOf__string"]
    """<p>S3 keys made available using this asset.</p>"""
    s3_access_point_alias: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The automatically-generated bucket-style alias for your Amazon S3 Access Point. Customers can access their entitled data using the S3 Access Point alias.</p>"""
    s3_access_point_arn: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The ARN for your Amazon S3 Access Point. Customers can also access their entitled data using the S3 Access Point ARN.</p>"""
    kms_keys_to_grant: NotRequired[
        "aws_sdk_dataexchange.types.list_of_kms_keys_to_grant.ListOfKmsKeysToGrant"
    ]
    """<p> List of AWS KMS CMKs (Key Management System Customer Managed Keys) and ARNs used to encrypt S3 objects being shared in this S3 Data Access asset. Providers must include all AWS KMS keys used to encrypt these shared S3 objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DataAccessAsset) -> dict:
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
    if "s3_access_point_alias" in value:
        out["S3AccessPointAlias"] = value["s3_access_point_alias"]
    if "s3_access_point_arn" in value:
        out["S3AccessPointArn"] = value["s3_access_point_arn"]
    if "kms_keys_to_grant" in value:
        import aws_sdk_dataexchange.types.list_of_kms_keys_to_grant

        out["KmsKeysToGrant"] = (
            aws_sdk_dataexchange.types.list_of_kms_keys_to_grant.serialize_json(
                value["kms_keys_to_grant"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3DataAccessAsset:
    out: S3DataAccessAsset = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("S3DataAccessAsset.bucket required")
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
    if "S3AccessPointAlias" in data:
        out["s3_access_point_alias"] = data["S3AccessPointAlias"]
    if "S3AccessPointArn" in data:
        out["s3_access_point_arn"] = data["S3AccessPointArn"]
    if "KmsKeysToGrant" in data:
        import aws_sdk_dataexchange.types.list_of_kms_keys_to_grant

        out["kms_keys_to_grant"] = (
            aws_sdk_dataexchange.types.list_of_kms_keys_to_grant.deserialize_json(
                data["KmsKeysToGrant"]
            )
        )
    return out
