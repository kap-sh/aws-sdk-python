"""Generated from Smithy shape ``com.amazonaws.kms#KeyListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.arn_type
    import capo_kms.types.key_id_type


class KeyListEntry(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>Unique identifier of the key.</p>"""
    key_arn: NotRequired["capo_kms.types.arn_type.ArnType"]
    """<p>ARN of the key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyListEntry) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_arn" in value:
        out["KeyArn"] = value["key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyListEntry:
    out: KeyListEntry = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    return out
