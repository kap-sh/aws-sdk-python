"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableEncryptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.encryption_configuration


class GetTableEncryptionResponse(TypedDict, closed=True):
    encryption_configuration: (
        "aws_sdk_s3tables.types.encryption_configuration.EncryptionConfiguration"
    )
    """<p>The encryption configuration for the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableEncryptionResponse) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.encryption_configuration

    out["encryptionConfiguration"] = (
        aws_sdk_s3tables.types.encryption_configuration.serialize_json(
            value["encryption_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableEncryptionResponse:
    out: GetTableEncryptionResponse = {}  # type: ignore[typeddict-item]
    if "encryptionConfiguration" in data:
        import aws_sdk_s3tables.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_s3tables.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableEncryptionResponse.encryption_configuration required"
        )
    return out
