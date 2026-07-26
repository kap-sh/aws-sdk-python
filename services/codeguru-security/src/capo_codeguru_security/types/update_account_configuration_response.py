"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#UpdateAccountConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguru_security.types.encryption_config


class UpdateAccountConfigurationResponse(TypedDict, closed=True):
    encryption_config: "capo_codeguru_security.types.encryption_config.EncryptionConfig"
    """<p>An <code>EncryptionConfig</code> object that contains the KMS key ARN that is used for encryption. If you did not specify a customer-managed KMS key in the request, returns empty. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountConfigurationResponse) -> dict:
    out: dict = {}
    import capo_codeguru_security.types.encryption_config

    out["encryptionConfig"] = (
        capo_codeguru_security.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAccountConfigurationResponse:
    out: UpdateAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "encryptionConfig" in data:
        import capo_codeguru_security.types.encryption_config

        out["encryption_config"] = (
            capo_codeguru_security.types.encryption_config.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccountConfigurationResponse.encryption_config required"
        )
    return out
