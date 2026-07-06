"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#EnableDefaultKeyReplicationRegionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.regions


class EnableDefaultKeyReplicationRegionsOutput(TypedDict, closed=True):
    enabled_replication_regions: "aws_sdk_payment_cryptography.types.regions.Regions"
    """<p>The complete list of regions where default key replication is now enabled for the account.</p> <p>This includes both previously enabled regions and the newly added regions from this operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnableDefaultKeyReplicationRegionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.regions

    out["EnabledReplicationRegions"] = (
        aws_sdk_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["enabled_replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnableDefaultKeyReplicationRegionsOutput:
    out: EnableDefaultKeyReplicationRegionsOutput = {}  # type: ignore[typeddict-item]
    if "EnabledReplicationRegions" in data:
        import aws_sdk_payment_cryptography.types.regions

        out["enabled_replication_regions"] = (
            aws_sdk_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["EnabledReplicationRegions"]
            )
        )
    else:
        raise DeserializationError(
            "EnableDefaultKeyReplicationRegionsOutput.enabled_replication_regions required"
        )
    return out
