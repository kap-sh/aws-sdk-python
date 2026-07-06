"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#AddKeyReplicationRegionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography.types.regions


class AddKeyReplicationRegionsInput(TypedDict, closed=True):
    key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The key identifier (ARN or alias) of the key for which to add replication regions.</p> <p>This key must exist and be in a valid state for replication operations.</p>"""
    replication_regions: "aws_sdk_payment_cryptography.types.regions.Regions"
    """<p>The list of Amazon Web Services Regions to add to the key's replication configuration.</p> <p>Each region must be a valid Amazon Web Services Region where Amazon Web Services Payment Cryptography is available. The key will be replicated to these regions, allowing cryptographic operations to be performed closer to your applications.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddKeyReplicationRegionsInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    import aws_sdk_payment_cryptography.types.regions

    out["ReplicationRegions"] = (
        aws_sdk_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddKeyReplicationRegionsInput:
    out: AddKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError(
            "AddKeyReplicationRegionsInput.key_identifier required"
        )
    if "ReplicationRegions" in data:
        import aws_sdk_payment_cryptography.types.regions

        out["replication_regions"] = (
            aws_sdk_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["ReplicationRegions"]
            )
        )
    else:
        raise DeserializationError(
            "AddKeyReplicationRegionsInput.replication_regions required"
        )
    return out
