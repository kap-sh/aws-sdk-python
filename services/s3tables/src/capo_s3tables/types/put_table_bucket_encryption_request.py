"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketEncryptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.table_bucket_arn


class PutTableBucketEncryptionRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    encryption_configuration: (
        "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
    )
    """<p>The encryption configuration to apply to the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketEncryptionRequest) -> dict:
    out: dict = {}
    import capo_s3tables.types.encryption_configuration

    out["encryptionConfiguration"] = (
        capo_s3tables.types.encryption_configuration.serialize_json(
            value["encryption_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableBucketEncryptionRequest:
    out: PutTableBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
    if "encryptionConfiguration" in data:
        import capo_s3tables.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3tables.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutTableBucketEncryptionRequest.encryption_configuration required"
        )
    return out
