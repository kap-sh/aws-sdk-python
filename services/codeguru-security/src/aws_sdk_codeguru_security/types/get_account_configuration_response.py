"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#GetAccountConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.encryption_config


class GetAccountConfigurationResponse(TypedDict, closed=True):
    encryption_config: (
        "aws_sdk_codeguru_security.types.encryption_config.EncryptionConfig"
    )
    """<p>An <code>EncryptionConfig</code> object that contains the KMS key ARN that is used for encryption. By default, CodeGuru Security uses an AWS-managed key for encryption. To specify your own key, call <code>UpdateAccountConfiguration</code>. If you do not specify a customer-managed key, returns empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguru_security.types.encryption_config

    out["encryptionConfig"] = (
        aws_sdk_codeguru_security.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAccountConfigurationResponse:
    out: GetAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "encryptionConfig" in data:
        import aws_sdk_codeguru_security.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_codeguru_security.types.encryption_config.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountConfigurationResponse.encryption_config required"
        )
    return out
