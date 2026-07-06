"""Generated from Smithy shape ``com.amazonaws.kafka#EncryptionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.encryption_at_rest
    import aws_sdk_kafka.types.encryption_in_transit


class EncryptionInfo(TypedDict, closed=True):
    encryption_at_rest: NotRequired[
        "aws_sdk_kafka.types.encryption_at_rest.EncryptionAtRest"
    ]
    """<p>The data-volume encryption details.</p>"""
    encryption_in_transit: NotRequired[
        "aws_sdk_kafka.types.encryption_in_transit.EncryptionInTransit"
    ]
    """<p>The details for encryption in transit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionInfo) -> dict:
    out: dict = {}
    if "encryption_at_rest" in value:
        import aws_sdk_kafka.types.encryption_at_rest

        out["encryptionAtRest"] = aws_sdk_kafka.types.encryption_at_rest.serialize_json(
            value["encryption_at_rest"]
        )
    if "encryption_in_transit" in value:
        import aws_sdk_kafka.types.encryption_in_transit

        out["encryptionInTransit"] = (
            aws_sdk_kafka.types.encryption_in_transit.serialize_json(
                value["encryption_in_transit"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionInfo:
    out: EncryptionInfo = {}  # type: ignore[typeddict-item]
    if "encryptionAtRest" in data:
        import aws_sdk_kafka.types.encryption_at_rest

        out["encryption_at_rest"] = (
            aws_sdk_kafka.types.encryption_at_rest.deserialize_json(
                data["encryptionAtRest"]
            )
        )
    if "encryptionInTransit" in data:
        import aws_sdk_kafka.types.encryption_in_transit

        out["encryption_in_transit"] = (
            aws_sdk_kafka.types.encryption_in_transit.deserialize_json(
                data["encryptionInTransit"]
            )
        )
    return out
