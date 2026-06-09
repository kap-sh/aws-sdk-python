"""Generated from Smithy shape ``com.amazonaws.kms#AliasListEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.alias_name_type
    import aws_sdk_kms.types.arn_type
    import aws_sdk_kms.types.date_type
    import aws_sdk_kms.types.key_id_type


class AliasListEntry(TypedDict):
    alias_name: NotRequired["aws_sdk_kms.types.alias_name_type.AliasNameType"]
    """<p>String that contains the alias. This value begins with <code>alias/</code>.</p>"""
    alias_arn: NotRequired["aws_sdk_kms.types.arn_type.ArnType"]
    """<p>String that contains the key ARN.</p>"""
    target_key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>String that contains the key identifier of the KMS key associated with the alias.</p>"""
    creation_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>Date and time that the alias was most recently created in the account and Region. Formatted as Unix time.</p>"""
    last_updated_date: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>Date and time that the alias was most recently associated with a KMS key in the account and Region. Formatted as Unix time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasListEntry) -> dict:
    out: dict = {}
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "alias_arn" in value:
        out["AliasArn"] = value["alias_arn"]
    if "target_key_id" in value:
        out["TargetKeyId"] = value["target_key_id"]
    if "creation_date" in value:
        import aws_sdk_kms.types.date_type

        out["CreationDate"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["creation_date"]
        )
    if "last_updated_date" in value:
        import aws_sdk_kms.types.date_type

        out["LastUpdatedDate"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["last_updated_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AliasListEntry:
    out: AliasListEntry = {}  # type: ignore[typeddict-item]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    if "AliasArn" in data:
        out["alias_arn"] = data["AliasArn"]
    if "TargetKeyId" in data:
        out["target_key_id"] = data["TargetKeyId"]
    if "CreationDate" in data:
        import aws_sdk_kms.types.date_type

        out["creation_date"] = aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
            data["CreationDate"]
        )
    if "LastUpdatedDate" in data:
        import aws_sdk_kms.types.date_type

        out["last_updated_date"] = aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
            data["LastUpdatedDate"]
        )
    return out
