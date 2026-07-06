"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslateKeyMaterialInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.incoming_key_material
    import aws_sdk_payment_cryptography_data.types.key_check_value_algorithm
    import aws_sdk_payment_cryptography_data.types.outgoing_key_material


class TranslateKeyMaterialInput(TypedDict, closed=True):
    incoming_key_material: "aws_sdk_payment_cryptography_data.types.incoming_key_material.IncomingKeyMaterial"
    """<p>Parameter information of the TR31WrappedKeyBlock containing the transaction key.</p>"""
    outgoing_key_material: "aws_sdk_payment_cryptography_data.types.outgoing_key_material.OutgoingKeyMaterial"
    """<p>Parameter information of the wrapping key used to wrap the transaction key in the outgoing TR31WrappedKeyBlock.</p>"""
    key_check_value_algorithm: NotRequired[
        "aws_sdk_payment_cryptography_data.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    ]
    """<p>The key check value (KCV) algorithm used for calculating the KCV of the derived key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslateKeyMaterialInput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.incoming_key_material

    out["IncomingKeyMaterial"] = (
        aws_sdk_payment_cryptography_data.types.incoming_key_material.serialize_json(
            value["incoming_key_material"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.outgoing_key_material

    out["OutgoingKeyMaterial"] = (
        aws_sdk_payment_cryptography_data.types.outgoing_key_material.serialize_json(
            value["outgoing_key_material"]
        )
    )
    if "key_check_value_algorithm" in value:
        out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    return out


def deserialize_json(data: dict) -> TranslateKeyMaterialInput:
    out: TranslateKeyMaterialInput = {}  # type: ignore[typeddict-item]
    if "IncomingKeyMaterial" in data:
        import aws_sdk_payment_cryptography_data.types.incoming_key_material

        out["incoming_key_material"] = (
            aws_sdk_payment_cryptography_data.types.incoming_key_material.deserialize_json(
                data["IncomingKeyMaterial"]
            )
        )
    else:
        raise DeserializationError(
            "TranslateKeyMaterialInput.incoming_key_material required"
        )
    if "OutgoingKeyMaterial" in data:
        import aws_sdk_payment_cryptography_data.types.outgoing_key_material

        out["outgoing_key_material"] = (
            aws_sdk_payment_cryptography_data.types.outgoing_key_material.deserialize_json(
                data["OutgoingKeyMaterial"]
            )
        )
    else:
        raise DeserializationError(
            "TranslateKeyMaterialInput.outgoing_key_material required"
        )
    if "KeyCheckValueAlgorithm" in data:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    return out
