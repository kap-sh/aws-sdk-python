"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DisableDefaultKeyReplicationRegionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.regions


class DisableDefaultKeyReplicationRegionsInput(TypedDict):
    replication_regions: "aws_sdk_payment_cryptography.types.regions.Regions"
    """<p>The list of Amazon Web Services Regions to remove from the account's default replication regions.</p> <p>New keys created after this operation will not automatically be replicated to these regions, though existing keys with replication to these regions will be unaffected.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisableDefaultKeyReplicationRegionsInput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.regions

    out["ReplicationRegions"] = (
        aws_sdk_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisableDefaultKeyReplicationRegionsInput:
    out: DisableDefaultKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
    if "ReplicationRegions" in data:
        import aws_sdk_payment_cryptography.types.regions

        out["replication_regions"] = (
            aws_sdk_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["ReplicationRegions"]
            )
        )
    else:
        raise DeserializationError(
            "DisableDefaultKeyReplicationRegionsInput.replication_regions required"
        )
    return out
