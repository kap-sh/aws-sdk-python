"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn
    import aws_sdk_payment_cryptography.types.key_attributes
    import aws_sdk_payment_cryptography.types.key_check_value
    import aws_sdk_payment_cryptography.types.key_state
    import aws_sdk_payment_cryptography.types.multi_region_key_type
    import aws_sdk_payment_cryptography.types.region


class KeySummary(TypedDict):
    key_arn: "aws_sdk_payment_cryptography.types.key_arn.KeyArn"
    """<p>The Amazon Resource Name (ARN) of the key.</p>"""
    key_state: "aws_sdk_payment_cryptography.types.key_state.KeyState"
    """<p>The state of an Amazon Web Services Payment Cryptography that is being created or deleted.</p>"""
    key_attributes: "aws_sdk_payment_cryptography.types.key_attributes.KeyAttributes"
    """<p>The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.</p>"""
    key_check_value: "aws_sdk_payment_cryptography.types.key_check_value.KeyCheckValue"
    """<p>The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p>"""
    exportable: "bool"
    """<p>Specifies whether the key is exportable. This data is immutable after the key is created.</p>"""
    enabled: "bool"
    """<p>Specifies whether the key is enabled. </p>"""
    multi_region_key_type: NotRequired[
        "aws_sdk_payment_cryptography.types.multi_region_key_type.MultiRegionKeyType"
    ]
    """<p>Indicates whether this key is a Multi-Region key and its role in the Multi-Region key hierarchy.</p> <p>Multi-Region replication keys allow the same key material to be used across multiple Amazon Web Services Regions. This field specifies whether the key is a Primary Region key (PRK) (which can be replicated to other Amazon Web Services Regions) or a Replica Region key (RRK) (which is a copy of a PRK in another Region). For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html\">Multi-Region key replication</a>.</p>"""
    primary_region: NotRequired["aws_sdk_payment_cryptography.types.region.Region"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeySummary) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyState"] = value["key_state"]
    import aws_sdk_payment_cryptography.types.key_attributes

    out["KeyAttributes"] = (
        aws_sdk_payment_cryptography.types.key_attributes.serialize_aws_json_1_0(
            value["key_attributes"]
        )
    )
    out["KeyCheckValue"] = value["key_check_value"]
    out["Exportable"] = value["exportable"]
    out["Enabled"] = value["enabled"]
    if "multi_region_key_type" in value:
        out["MultiRegionKeyType"] = value["multi_region_key_type"]
    if "primary_region" in value:
        out["PrimaryRegion"] = value["primary_region"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KeySummary:
    out: KeySummary = {}  # type: ignore[typeddict-item]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("KeySummary.key_arn required")
    if "KeyState" in data:
        out["key_state"] = data["KeyState"]
    else:
        raise DeserializationError("KeySummary.key_state required")
    if "KeyAttributes" in data:
        import aws_sdk_payment_cryptography.types.key_attributes

        out["key_attributes"] = (
            aws_sdk_payment_cryptography.types.key_attributes.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("KeySummary.key_attributes required")
    if "KeyCheckValue" in data:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        raise DeserializationError("KeySummary.key_check_value required")
    if "Exportable" in data:
        out["exportable"] = data["Exportable"]
    else:
        raise DeserializationError("KeySummary.exportable required")
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("KeySummary.enabled required")
    if "MultiRegionKeyType" in data:
        out["multi_region_key_type"] = data["MultiRegionKeyType"]
    if "PrimaryRegion" in data:
        out["primary_region"] = data["PrimaryRegion"]
    return out
