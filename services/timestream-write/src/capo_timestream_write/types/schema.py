"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Schema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.partition_key_list


class Schema(TypedDict, closed=True):
    composite_partition_key: NotRequired[
        "capo_timestream_write.types.partition_key_list.PartitionKeyList"
    ]
    """<p>A non-empty list of partition keys defining the attributes used to partition the table data. The order of the list determines the partition hierarchy. The name and type of each partition key as well as the partition key order cannot be changed after the table is created. However, the enforcement level of each partition key can be changed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Schema) -> dict:
    out: dict = {}
    if "composite_partition_key" in value:
        import capo_timestream_write.types.partition_key_list

        out["CompositePartitionKey"] = (
            capo_timestream_write.types.partition_key_list.serialize_aws_json_1_0(
                value["composite_partition_key"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Schema:
    out: Schema = {}  # type: ignore[typeddict-item]
    if "CompositePartitionKey" in data:
        import capo_timestream_write.types.partition_key_list

        out["composite_partition_key"] = (
            capo_timestream_write.types.partition_key_list.deserialize_aws_json_1_0(
                data["CompositePartitionKey"]
            )
        )
    return out
