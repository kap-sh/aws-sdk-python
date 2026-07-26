"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketEncryptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.encryption_configuration


class GetTableBucketEncryptionResponse(TypedDict, closed=True):
    encryption_configuration: (
        "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
    )
    """<p>The encryption configuration for the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketEncryptionResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.encryption_configuration

    out["encryptionConfiguration"] = (
        capo_s3tables.types.encryption_configuration.serialize_json(
            value["encryption_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableBucketEncryptionResponse:
    out: GetTableBucketEncryptionResponse = {}  # type: ignore[typeddict-item]
    if "encryptionConfiguration" in data:
        import capo_s3tables.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3tables.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableBucketEncryptionResponse.encryption_configuration required"
        )
    return out
