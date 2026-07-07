"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDataset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_supplychain.types.asc_resource_arn
    import aws_sdk_supplychain.types.data_lake_dataset_description
    import aws_sdk_supplychain.types.data_lake_dataset_name
    import aws_sdk_supplychain.types.data_lake_dataset_partition_spec
    import aws_sdk_supplychain.types.data_lake_dataset_schema
    import aws_sdk_supplychain.types.data_lake_namespace_name
    import aws_sdk_supplychain.types.uuid


class DataLakeDataset(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    namespace: (
        "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    )
    r"""<p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>"""
    name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName"
    r"""<p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>"""
    arn: "aws_sdk_supplychain.types.asc_resource_arn.AscResourceArn"
    """<p>The arn of the dataset.</p>"""
    schema: "aws_sdk_supplychain.types.data_lake_dataset_schema.DataLakeDatasetSchema"
    """<p>The schema of the dataset.</p>"""
    description: NotRequired[
        "aws_sdk_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"
    ]
    """<p>The description of the dataset.</p>"""
    partition_spec: NotRequired[
        "aws_sdk_supplychain.types.data_lake_dataset_partition_spec.DataLakeDatasetPartitionSpec"
    ]
    created_time: "datetime.datetime"
    """<p>The creation time of the dataset.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The last modified time of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDataset) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["namespace"] = value["namespace"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import aws_sdk_supplychain.types.data_lake_dataset_schema

    out["schema"] = aws_sdk_supplychain.types.data_lake_dataset_schema.serialize_json(
        value["schema"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "partition_spec" in value:
        import aws_sdk_supplychain.types.data_lake_dataset_partition_spec

        out["partitionSpec"] = (
            aws_sdk_supplychain.types.data_lake_dataset_partition_spec.serialize_json(
                value["partition_spec"]
            )
        )
    import aws_sdk_supplychain.types._prelude.timestamp

    out["createdTime"] = aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_supplychain.types._prelude.timestamp

    out["lastModifiedTime"] = (
        aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataLakeDataset:
    out: DataLakeDataset = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("DataLakeDataset.instance_id required")
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("DataLakeDataset.namespace required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataLakeDataset.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DataLakeDataset.arn required")
    if "schema" in data:
        import aws_sdk_supplychain.types.data_lake_dataset_schema

        out["schema"] = (
            aws_sdk_supplychain.types.data_lake_dataset_schema.deserialize_json(
                data["schema"]
            )
        )
    else:
        raise DeserializationError("DataLakeDataset.schema required")
    if "description" in data:
        out["description"] = data["description"]
    if "partitionSpec" in data:
        import aws_sdk_supplychain.types.data_lake_dataset_partition_spec

        out["partition_spec"] = (
            aws_sdk_supplychain.types.data_lake_dataset_partition_spec.deserialize_json(
                data["partitionSpec"]
            )
        )
    if "createdTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("DataLakeDataset.created_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("DataLakeDataset.last_modified_time required")
    return out
