"""Generated from Smithy shape ``com.amazonaws.greengrass#SecretsManagerSecretResourceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of__string
    import aws_sdk_greengrass.types.__string


class SecretsManagerSecretResourceData(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the Secrets Manager secret to make available on the core. The value of the secret's latest version (represented by the ''AWSCURRENT'' staging label) is included by default."""
    additional_staging_labels_to_download: NotRequired[
        "aws_sdk_greengrass.types.__list_of__string.__listOf__string"
    ]
    """Optional. The staging labels whose values you want to make available on the core, in addition to ''AWSCURRENT''."""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerSecretResourceData) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "additional_staging_labels_to_download" in value:
        import aws_sdk_greengrass.types.__list_of__string

        out["AdditionalStagingLabelsToDownload"] = (
            aws_sdk_greengrass.types.__list_of__string.serialize_json(
                value["additional_staging_labels_to_download"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecretsManagerSecretResourceData:
    out: SecretsManagerSecretResourceData = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "AdditionalStagingLabelsToDownload" in data:
        import aws_sdk_greengrass.types.__list_of__string

        out["additional_staging_labels_to_download"] = (
            aws_sdk_greengrass.types.__list_of__string.deserialize_json(
                data["AdditionalStagingLabelsToDownload"]
            )
        )
    return out
