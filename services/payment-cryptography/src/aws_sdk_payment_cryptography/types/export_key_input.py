"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.export_attributes
    import aws_sdk_payment_cryptography.types.export_key_material
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type


class ExportKeyInput(TypedDict, closed=True):
    key_material: (
        "aws_sdk_payment_cryptography.types.export_key_material.ExportKeyMaterial"
    )
    """<p>The key block format type, for example, TR-34 or TR-31, to use during key material export.</p>"""
    export_key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>KeyARN</code> of the key under export from Amazon Web Services Payment Cryptography.</p>"""
    export_attributes: NotRequired[
        "aws_sdk_payment_cryptography.types.export_attributes.ExportAttributes"
    ]
    """<p>The attributes for IPEK generation during export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportKeyInput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.export_key_material

    out["KeyMaterial"] = (
        aws_sdk_payment_cryptography.types.export_key_material.serialize_aws_json_1_0(
            value["key_material"]
        )
    )
    out["ExportKeyIdentifier"] = value["export_key_identifier"]
    if "export_attributes" in value:
        import aws_sdk_payment_cryptography.types.export_attributes

        out["ExportAttributes"] = (
            aws_sdk_payment_cryptography.types.export_attributes.serialize_aws_json_1_0(
                value["export_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportKeyInput:
    out: ExportKeyInput = {}  # type: ignore[typeddict-item]
    if "KeyMaterial" in data:
        import aws_sdk_payment_cryptography.types.export_key_material

        out["key_material"] = (
            aws_sdk_payment_cryptography.types.export_key_material.deserialize_aws_json_1_0(
                data["KeyMaterial"]
            )
        )
    else:
        raise DeserializationError("ExportKeyInput.key_material required")
    if "ExportKeyIdentifier" in data:
        out["export_key_identifier"] = data["ExportKeyIdentifier"]
    else:
        raise DeserializationError("ExportKeyInput.export_key_identifier required")
    if "ExportAttributes" in data:
        import aws_sdk_payment_cryptography.types.export_attributes

        out["export_attributes"] = (
            aws_sdk_payment_cryptography.types.export_attributes.deserialize_aws_json_1_0(
                data["ExportAttributes"]
            )
        )
    return out
