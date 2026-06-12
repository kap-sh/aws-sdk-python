"""Generated from Smithy shape ``com.amazonaws.xray#GetEncryptionConfigResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.encryption_config


class GetEncryptionConfigResult(TypedDict):
    encryption_config: NotRequired[
        "aws_sdk_xray.types.encryption_config.EncryptionConfig"
    ]
    """<p>The encryption configuration document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEncryptionConfigResult) -> dict:
    out: dict = {}
    if "encryption_config" in value:
        import aws_sdk_xray.types.encryption_config

        out["EncryptionConfig"] = aws_sdk_xray.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    return out


def deserialize_json(data: dict) -> GetEncryptionConfigResult:
    out: GetEncryptionConfigResult = {}  # type: ignore[typeddict-item]
    if "EncryptionConfig" in data:
        import aws_sdk_xray.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_xray.types.encryption_config.deserialize_json(
                data["EncryptionConfig"]
            )
        )
    return out
