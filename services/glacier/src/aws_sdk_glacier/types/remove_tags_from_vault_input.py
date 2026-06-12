"""Generated from Smithy shape ``com.amazonaws.glacier#RemoveTagsFromVaultInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string
    import aws_sdk_glacier.types.tag_key_list


class RemoveTagsFromVaultInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    tag_keys: NotRequired["aws_sdk_glacier.types.tag_key_list.TagKeyList"]
    """<p>A list of tag keys. Each corresponding tag is removed from the vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveTagsFromVaultInput) -> dict:
    out: dict = {}
    if "tag_keys" in value:
        import aws_sdk_glacier.types.tag_key_list

        out["TagKeys"] = aws_sdk_glacier.types.tag_key_list.serialize_json(
            value["tag_keys"]
        )
    return out


def deserialize_json(data: dict) -> RemoveTagsFromVaultInput:
    out: RemoveTagsFromVaultInput = {}  # type: ignore[typeddict-item]
    if "TagKeys" in data:
        import aws_sdk_glacier.types.tag_key_list

        out["tag_keys"] = aws_sdk_glacier.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    return out
