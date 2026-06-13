"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#UpdateAccountConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.encryption_config


class UpdateAccountConfigurationRequest(TypedDict):
    encryption_config: (
        "aws_sdk_codeguru_security.types.encryption_config.EncryptionConfig"
    )
    """<p>The customer-managed KMS key ARN you want to use for encryption. If not specified, CodeGuru Security will use an AWS-managed key for encryption. If you previously specified a customer-managed KMS key and want CodeGuru Security to use an AWS-managed key for encryption instead, pass nothing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_codeguru_security.types.encryption_config

    out["encryptionConfig"] = (
        aws_sdk_codeguru_security.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAccountConfigurationRequest:
    out: UpdateAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "encryptionConfig" in data:
        import aws_sdk_codeguru_security.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_codeguru_security.types.encryption_config.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccountConfigurationRequest.encryption_config required"
        )
    return out
