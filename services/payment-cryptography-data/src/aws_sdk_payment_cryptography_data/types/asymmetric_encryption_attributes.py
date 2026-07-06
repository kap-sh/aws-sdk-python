"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#AsymmetricEncryptionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.padding_type


class AsymmetricEncryptionAttributes(TypedDict, closed=True):
    padding_type: NotRequired[
        "aws_sdk_payment_cryptography_data.types.padding_type.PaddingType"
    ]
    """<p>The padding to be included with the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AsymmetricEncryptionAttributes) -> dict:
    out: dict = {}
    if "padding_type" in value:
        import aws_sdk_payment_cryptography_data.types.padding_type

        out["PaddingType"] = (
            aws_sdk_payment_cryptography_data.types.padding_type.serialize_json(
                value["padding_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AsymmetricEncryptionAttributes:
    out: AsymmetricEncryptionAttributes = {}  # type: ignore[typeddict-item]
    if "PaddingType" in data:
        import aws_sdk_payment_cryptography_data.types.padding_type

        out["padding_type"] = (
            aws_sdk_payment_cryptography_data.types.padding_type.deserialize_json(
                data["PaddingType"]
            )
        )
    return out
