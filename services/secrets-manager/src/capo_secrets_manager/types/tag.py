"""Generated from Smithy shape ``com.amazonaws.secretsmanager#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.tag_key_type
    import capo_secrets_manager.types.tag_value_type


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_secrets_manager.types.tag_key_type.TagKeyType"]
    """<p>The key identifier, or name, of the tag.</p>"""
    value: NotRequired["capo_secrets_manager.types.tag_value_type.TagValueType"]
    """<p>The string value associated with the key of the tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
