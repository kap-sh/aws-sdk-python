"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#AddKeyReplicationRegionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key


class AddKeyReplicationRegionsOutput(TypedDict, closed=True):
    key: "capo_payment_cryptography.types.key.Key"
    """<p>The updated key metadata after adding the replication regions.</p> <p>This includes the current state of the key and its replication configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddKeyReplicationRegionsOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.key

    out["Key"] = capo_payment_cryptography.types.key.serialize_aws_json_1_0(
        value["key"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddKeyReplicationRegionsOutput:
    out: AddKeyReplicationRegionsOutput = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import capo_payment_cryptography.types.key

        out["key"] = capo_payment_cryptography.types.key.deserialize_aws_json_1_0(
            data["Key"]
        )
    else:
        raise DeserializationError("AddKeyReplicationRegionsOutput.key required")
    return out
