"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#RemoveKeyReplicationRegionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography.types.regions


class RemoveKeyReplicationRegionsInput(TypedDict):
    key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The key identifier (ARN or alias) of the key from which to remove replication regions.</p> <p>This key must exist and have replication enabled in the specified regions.</p>"""
    replication_regions: "aws_sdk_payment_cryptography.types.regions.Regions"
    """<p>The list of Amazon Web Services Regions to remove from the key's replication configuration.</p> <p>The key will no longer be available for cryptographic operations in these regions after removal. Ensure no active operations depend on the key in these regions before removal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RemoveKeyReplicationRegionsInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    import aws_sdk_payment_cryptography.types.regions

    out["ReplicationRegions"] = (
        aws_sdk_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RemoveKeyReplicationRegionsInput:
    out: RemoveKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError(
            "RemoveKeyReplicationRegionsInput.key_identifier required"
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
            "RemoveKeyReplicationRegionsInput.replication_regions required"
        )
    return out
