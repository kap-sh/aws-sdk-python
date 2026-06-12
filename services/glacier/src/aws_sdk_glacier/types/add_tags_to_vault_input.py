"""Generated from Smithy shape ``com.amazonaws.glacier#AddTagsToVaultInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string
    import aws_sdk_glacier.types.tag_map


class AddTagsToVaultInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    tags: NotRequired["aws_sdk_glacier.types.tag_map.TagMap"]
    """<p>The tags to add to the vault. Each tag is composed of a key and a value. The value can be an empty string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddTagsToVaultInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_glacier.types.tag_map

        out["Tags"] = aws_sdk_glacier.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AddTagsToVaultInput:
    out: AddTagsToVaultInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_glacier.types.tag_map

        out["tags"] = aws_sdk_glacier.types.tag_map.deserialize_json(data["Tags"])
    return out
