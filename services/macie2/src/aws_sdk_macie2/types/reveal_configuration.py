"""Generated from Smithy shape ``com.amazonaws.macie2#RevealConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string_min1_max2048
    import aws_sdk_macie2.types.reveal_status


class RevealConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired[
        "aws_sdk_macie2.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """<p>The Amazon Resource Name (ARN), ID, or alias of the KMS key to use to encrypt sensitive data that's retrieved. The key must be an existing, customer managed, symmetric encryption key that's enabled in the same Amazon Web Services Region as the Amazon Macie account.</p> <p>If this value specifies an alias, it must include the following prefix: alias/. If this value specifies a key that's owned by another Amazon Web Services account, it must specify the ARN of the key or the ARN of the key's alias.</p>"""
    status: NotRequired["aws_sdk_macie2.types.reveal_status.RevealStatus"]
    """<p>The status of the configuration for the Amazon Macie account. In a response, possible values are: ENABLED, the configuration is currently enabled for the account; and, DISABLED, the configuration is currently disabled for the account. In a request, valid values are: ENABLED, enable the configuration for the account; and, DISABLED, disable the configuration for the account.</p> <important><p>If you disable the configuration, you also permanently delete current settings that specify how to access affected S3 objects. If your current access method is ASSUME_ROLE, Macie also deletes the external ID and role name currently specified for the configuration. These settings can't be recovered after they're deleted.</p></important>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevealConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "status" in value:
        import aws_sdk_macie2.types.reveal_status

        out["status"] = aws_sdk_macie2.types.reveal_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> RevealConfiguration:
    out: RevealConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "status" in data:
        import aws_sdk_macie2.types.reveal_status

        out["status"] = aws_sdk_macie2.types.reveal_status.deserialize_json(
            data["status"]
        )
    return out
