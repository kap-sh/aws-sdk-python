"""Generated from Smithy shape ``com.amazonaws.eks#EncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.provider
    import aws_sdk_eks.types.string_list


class EncryptionConfig(TypedDict, closed=True):
    resources: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>Specifies the resources to be encrypted. The only supported value is <code>secrets</code>.</p>"""
    provider: NotRequired["aws_sdk_eks.types.provider.Provider"]
    """<p>Key Management Service (KMS) key. Either the ARN or the alias can be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfig) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_eks.types.string_list

        out["resources"] = aws_sdk_eks.types.string_list.serialize_json(
            value["resources"]
        )
    if "provider" in value:
        import aws_sdk_eks.types.provider

        out["provider"] = aws_sdk_eks.types.provider.serialize_json(value["provider"])
    return out


def deserialize_json(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import aws_sdk_eks.types.string_list

        out["resources"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["resources"]
        )
    if "provider" in data:
        import aws_sdk_eks.types.provider

        out["provider"] = aws_sdk_eks.types.provider.deserialize_json(data["provider"])
    return out
