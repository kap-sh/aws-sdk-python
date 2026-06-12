"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ReplicationStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.region
    import aws_sdk_payment_cryptography.types.replication_status_type

ReplicationStatus: TypeAlias = dict[
    "aws_sdk_payment_cryptography.types.region.Region",
    "aws_sdk_payment_cryptography.types.replication_status_type.ReplicationStatusType",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ReplicationStatus) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_payment_cryptography.types.replication_status_type

        out[key] = (
            aws_sdk_payment_cryptography.types.replication_status_type.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationStatus:
    out: ReplicationStatus = {}
    for key, value in data.items():
        import aws_sdk_payment_cryptography.types.replication_status_type

        out[key] = (
            aws_sdk_payment_cryptography.types.replication_status_type.deserialize_aws_json_1_0(
                value
            )
        )
    return out
