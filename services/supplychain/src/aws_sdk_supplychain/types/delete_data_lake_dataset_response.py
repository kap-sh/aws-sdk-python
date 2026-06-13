"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteDataLakeDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset_name
    import aws_sdk_supplychain.types.data_lake_namespace_name
    import aws_sdk_supplychain.types.uuid


class DeleteDataLakeDatasetResponse(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    namespace: (
        "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    )
    """<p>The namespace of deleted dataset.</p>"""
    name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName"
    """<p>The name of deleted dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataLakeDatasetResponse) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["namespace"] = value["namespace"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteDataLakeDatasetResponse:
    out: DeleteDataLakeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("DeleteDataLakeDatasetResponse.instance_id required")
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("DeleteDataLakeDatasetResponse.namespace required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteDataLakeDatasetResponse.name required")
    return out
