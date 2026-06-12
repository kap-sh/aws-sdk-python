"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Encryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.sse_algorithm


class Encryption(TypedDict):
    sse_algorithm: "aws_sdk_observabilityadmin.types.sse_algorithm.SSEAlgorithm"
    """<p>The server-side encryption algorithm used for encrypting data in the S3 Table integration.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used for encryption when using customer-managed keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Encryption) -> dict:
    out: dict = {}
    import aws_sdk_observabilityadmin.types.sse_algorithm

    out["SseAlgorithm"] = aws_sdk_observabilityadmin.types.sse_algorithm.serialize_json(
        value["sse_algorithm"]
    )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> Encryption:
    out: Encryption = {}  # type: ignore[typeddict-item]
    if "SseAlgorithm" in data:
        import aws_sdk_observabilityadmin.types.sse_algorithm

        out["sse_algorithm"] = (
            aws_sdk_observabilityadmin.types.sse_algorithm.deserialize_json(
                data["SseAlgorithm"]
            )
        )
    else:
        raise DeserializationError("Encryption.sse_algorithm required")
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
