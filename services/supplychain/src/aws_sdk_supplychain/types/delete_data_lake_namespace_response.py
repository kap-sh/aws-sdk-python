"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteDataLakeNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_namespace_name
    import aws_sdk_supplychain.types.uuid


class DeleteDataLakeNamespaceResponse(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The name of deleted namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataLakeNamespaceResponse) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteDataLakeNamespaceResponse:
    out: DeleteDataLakeNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError(
            "DeleteDataLakeNamespaceResponse.instance_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteDataLakeNamespaceResponse.name required")
    return out
