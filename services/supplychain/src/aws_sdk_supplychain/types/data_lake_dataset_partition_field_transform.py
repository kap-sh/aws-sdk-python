"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPartitionFieldTransform``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset_partition_transform_type


class DataLakeDatasetPartitionFieldTransform(TypedDict, closed=True):
    type: "aws_sdk_supplychain.types.data_lake_dataset_partition_transform_type.DataLakeDatasetPartitionTransformType"
    """<p>The type of partitioning transformation for this field. The available options are:</p> <ul> <li> <p> <b>IDENTITY</b> - Partitions data on a given field by its exact values.</p> </li> <li> <p> <b>YEAR</b> - Partitions data on a timestamp field using year granularity.</p> </li> <li> <p> <b>MONTH</b> - Partitions data on a timestamp field using month granularity.</p> </li> <li> <p> <b>DAY</b> - Partitions data on a timestamp field using day granularity.</p> </li> <li> <p> <b>HOUR</b> - Partitions data on a timestamp field using hour granularity.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPartitionFieldTransform) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_lake_dataset_partition_transform_type

    out["type"] = (
        aws_sdk_supplychain.types.data_lake_dataset_partition_transform_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataLakeDatasetPartitionFieldTransform:
    out: DataLakeDatasetPartitionFieldTransform = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_supplychain.types.data_lake_dataset_partition_transform_type

        out["type"] = (
            aws_sdk_supplychain.types.data_lake_dataset_partition_transform_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "DataLakeDatasetPartitionFieldTransform.type required"
        )
    return out
