"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#RegisterUsageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.non_empty_string
    import aws_sdk_marketplace_metering.types.timestamp


class RegisterUsageResult(TypedDict):
    public_key_rotation_timestamp: NotRequired[
        "aws_sdk_marketplace_metering.types.timestamp.Timestamp"
    ]
    """<p>(Optional) Only included when public key version has expired</p>"""
    signature: NotRequired[
        "aws_sdk_marketplace_metering.types.non_empty_string.NonEmptyString"
    ]
    """<p>JWT Token</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterUsageResult) -> dict:
    out: dict = {}
    if "public_key_rotation_timestamp" in value:
        import aws_sdk_marketplace_metering.types.timestamp

        out["PublicKeyRotationTimestamp"] = (
            aws_sdk_marketplace_metering.types.timestamp.serialize_aws_json_1_1(
                value["public_key_rotation_timestamp"]
            )
        )
    if "signature" in value:
        out["Signature"] = value["signature"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterUsageResult:
    out: RegisterUsageResult = {}  # type: ignore[typeddict-item]
    if "PublicKeyRotationTimestamp" in data:
        import aws_sdk_marketplace_metering.types.timestamp

        out["public_key_rotation_timestamp"] = (
            aws_sdk_marketplace_metering.types.timestamp.deserialize_aws_json_1_1(
                data["PublicKeyRotationTimestamp"]
            )
        )
    if "Signature" in data:
        out["signature"] = data["Signature"]
    return out
