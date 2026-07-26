"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.multi_region_key
    import capo_kms.types.multi_region_key_list
    import capo_kms.types.multi_region_key_type


class MultiRegionConfiguration(TypedDict, closed=True):
    multi_region_key_type: NotRequired[
        "capo_kms.types.multi_region_key_type.MultiRegionKeyType"
    ]
    """<p>Indicates whether the KMS key is a <code>PRIMARY</code> or <code>REPLICA</code> key.</p>"""
    primary_key: NotRequired["capo_kms.types.multi_region_key.MultiRegionKey"]
    """<p>Displays the key ARN and Region of the primary key. This field includes the current KMS key if it is the primary key.</p>"""
    replica_keys: NotRequired["capo_kms.types.multi_region_key_list.MultiRegionKeyList"]
    """<p>displays the key ARNs and Regions of all replica keys. This field includes the current KMS key if it is a replica key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionConfiguration) -> dict:
    out: dict = {}
    if "multi_region_key_type" in value:
        import capo_kms.types.multi_region_key_type

        out["MultiRegionKeyType"] = (
            capo_kms.types.multi_region_key_type.serialize_aws_json_1_1(
                value["multi_region_key_type"]
            )
        )
    if "primary_key" in value:
        import capo_kms.types.multi_region_key

        out["PrimaryKey"] = capo_kms.types.multi_region_key.serialize_aws_json_1_1(
            value["primary_key"]
        )
    if "replica_keys" in value:
        import capo_kms.types.multi_region_key_list

        out["ReplicaKeys"] = (
            capo_kms.types.multi_region_key_list.serialize_aws_json_1_1(
                value["replica_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiRegionConfiguration:
    out: MultiRegionConfiguration = {}  # type: ignore[typeddict-item]
    if "MultiRegionKeyType" in data:
        import capo_kms.types.multi_region_key_type

        out["multi_region_key_type"] = (
            capo_kms.types.multi_region_key_type.deserialize_aws_json_1_1(
                data["MultiRegionKeyType"]
            )
        )
    if "PrimaryKey" in data:
        import capo_kms.types.multi_region_key

        out["primary_key"] = capo_kms.types.multi_region_key.deserialize_aws_json_1_1(
            data["PrimaryKey"]
        )
    if "ReplicaKeys" in data:
        import capo_kms.types.multi_region_key_list

        out["replica_keys"] = (
            capo_kms.types.multi_region_key_list.deserialize_aws_json_1_1(
                data["ReplicaKeys"]
            )
        )
    return out
