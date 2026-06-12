"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateDataLakeDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset_description
    import aws_sdk_supplychain.types.data_lake_dataset_name
    import aws_sdk_supplychain.types.data_lake_dataset_partition_spec
    import aws_sdk_supplychain.types.data_lake_dataset_schema
    import aws_sdk_supplychain.types.data_lake_namespace_name
    import aws_sdk_supplychain.types.tag_map
    import aws_sdk_supplychain.types.uuid

class CreateDataLakeDatasetRequest(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>"""
    name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName"
    """<p>The name of the dataset. For <b>asc</b> name space, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>"""
    schema: NotRequired["aws_sdk_supplychain.types.data_lake_dataset_schema.DataLakeDatasetSchema"]
    """<p>The custom schema of the data lake dataset and required for dataset in <b>default</b> and custom namespaces.</p>"""
    description: NotRequired["aws_sdk_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"]
    """<p>The description of the dataset.</p>"""
    partition_spec: NotRequired["aws_sdk_supplychain.types.data_lake_dataset_partition_spec.DataLakeDatasetPartitionSpec"]
    """<p>The partition specification of the dataset. Partitioning can effectively improve the dataset query performance by reducing the amount of data scanned during query execution. But partitioning or not will affect how data get ingested by data ingestion methods, such as SendDataIntegrationEvent's dataset UPSERT will upsert records within partition (instead of within whole dataset). For more details, refer to those data ingestion documentations.</p>"""
    tags: NotRequired["aws_sdk_supplychain.types.tag_map.TagMap"]
    """<p>The tags of the dataset.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateDataLakeDatasetRequest) -> dict:
    out: dict = {}
    if "schema" in value:
        import aws_sdk_supplychain.types.data_lake_dataset_schema
        out["schema"] = aws_sdk_supplychain.types.data_lake_dataset_schema.serialize_json(value["schema"])
    if "description" in value:
        out["description"] = value["description"]
    if "partition_spec" in value:
        import aws_sdk_supplychain.types.data_lake_dataset_partition_spec
        out["partitionSpec"] = aws_sdk_supplychain.types.data_lake_dataset_partition_spec.serialize_json(value["partition_spec"])
    if "tags" in value:
        import aws_sdk_supplychain.types.tag_map
        out["tags"] = aws_sdk_supplychain.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataLakeDatasetRequest:
    out: CreateDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        import aws_sdk_supplychain.types.data_lake_dataset_schema
        out["schema"] = aws_sdk_supplychain.types.data_lake_dataset_schema.deserialize_json(data["schema"])
    if "description" in data:
        out["description"] = data["description"]
    if "partitionSpec" in data:
        import aws_sdk_supplychain.types.data_lake_dataset_partition_spec
        out["partition_spec"] = aws_sdk_supplychain.types.data_lake_dataset_partition_spec.deserialize_json(data["partitionSpec"])
    if "tags" in data:
        import aws_sdk_supplychain.types.tag_map
        out["tags"] = aws_sdk_supplychain.types.tag_map.deserialize_json(data["tags"])
    return out