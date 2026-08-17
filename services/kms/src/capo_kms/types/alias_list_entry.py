"""Generated from Smithy shape ``com.amazonaws.kms#AliasListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.alias_name_type
    import capo_kms.types.arn_type
    import capo_kms.types.date_type
    import capo_kms.types.key_id_type


class AliasListEntry(TypedDict, closed=True):
    alias_name: NotRequired["capo_kms.types.alias_name_type.AliasNameType"]
    """<p>String that contains the alias. This value begins with <code>alias/</code>.</p>"""
    alias_arn: NotRequired["capo_kms.types.arn_type.ArnType"]
    """<p>String that contains the key ARN.</p>"""
    target_key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>String that contains the key identifier of the KMS key associated with the alias.</p>"""
    creation_date: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>Date and time that the alias was most recently created in the account and Region. Formatted as Unix time.</p>"""
    last_updated_date: NotRequired["capo_kms.types.date_type.DateType"]
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
        import capo_kms.types.date_type

        out["CreationDate"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["creation_date"]
        )
    if "last_updated_date" in value:
        import capo_kms.types.date_type

        out["LastUpdatedDate"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["last_updated_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AliasListEntry:
    out: AliasListEntry = {}  # type: ignore[typeddict-item]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    if data.get("AliasArn") is not None:
        out["alias_arn"] = data["AliasArn"]
    if data.get("TargetKeyId") is not None:
        out["target_key_id"] = data["TargetKeyId"]
    if data.get("CreationDate") is not None:
        import capo_kms.types.date_type

        out["creation_date"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["CreationDate"]
        )
    if data.get("LastUpdatedDate") is not None:
        import capo_kms.types.date_type

        out["last_updated_date"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["LastUpdatedDate"]
        )
    return out
