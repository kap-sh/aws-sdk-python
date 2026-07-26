"""Generated from Smithy shape ``com.amazonaws.xray#PutEncryptionConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.encryption_config


class PutEncryptionConfigResult(TypedDict, closed=True):
    encryption_config: NotRequired["capo_xray.types.encryption_config.EncryptionConfig"]
    """<p>The new encryption configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEncryptionConfigResult) -> dict:
    out: dict = {}
    if "encryption_config" in value:
        import capo_xray.types.encryption_config

        out["EncryptionConfig"] = capo_xray.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    return out


def deserialize_json(data: dict) -> PutEncryptionConfigResult:
    out: PutEncryptionConfigResult = {}  # type: ignore[typeddict-item]
    if "EncryptionConfig" in data:
        import capo_xray.types.encryption_config

        out["encryption_config"] = capo_xray.types.encryption_config.deserialize_json(
            data["EncryptionConfig"]
        )
    return out
