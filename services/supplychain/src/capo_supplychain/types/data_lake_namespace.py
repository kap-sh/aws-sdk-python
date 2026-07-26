"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeNamespace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_supplychain.types.asc_resource_arn
    import capo_supplychain.types.data_lake_namespace_description
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.uuid


class DataLakeNamespace(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The name of the namespace.</p>"""
    arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn"
    """<p>The arn of the namespace.</p>"""
    description: NotRequired[
        "capo_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
    ]
    """<p>The description of the namespace.</p>"""
    created_time: "datetime.datetime"
    """<p>The creation time of the namespace.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The last modified time of the namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeNamespace) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_supplychain.types._prelude.timestamp

    out["createdTime"] = capo_supplychain.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_supplychain.types._prelude.timestamp

    out["lastModifiedTime"] = capo_supplychain.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    return out


def deserialize_json(data: dict) -> DataLakeNamespace:
    out: DataLakeNamespace = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("DataLakeNamespace.instance_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataLakeNamespace.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DataLakeNamespace.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdTime" in data:
        import capo_supplychain.types._prelude.timestamp

        out["created_time"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("DataLakeNamespace.created_time required")
    if "lastModifiedTime" in data:
        import capo_supplychain.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("DataLakeNamespace.last_modified_time required")
    return out
