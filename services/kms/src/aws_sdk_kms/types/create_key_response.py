"""Generated from Smithy shape ``com.amazonaws.kms#CreateKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_metadata


class CreateKeyResponse(TypedDict):
    key_metadata: NotRequired["aws_sdk_kms.types.key_metadata.KeyMetadata"]
    """<p>Metadata associated with the KMS key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateKeyResponse) -> dict:
    out: dict = {}
    if "key_metadata" in value:
        import aws_sdk_kms.types.key_metadata

        out["KeyMetadata"] = aws_sdk_kms.types.key_metadata.serialize_aws_json_1_1(
            value["key_metadata"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateKeyResponse:
    out: CreateKeyResponse = {}  # type: ignore[typeddict-item]
    if "KeyMetadata" in data:
        import aws_sdk_kms.types.key_metadata

        out["key_metadata"] = aws_sdk_kms.types.key_metadata.deserialize_aws_json_1_1(
            data["KeyMetadata"]
        )
    return out
