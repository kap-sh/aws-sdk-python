"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftStorageProperties``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError


class _RedshiftStorageProperties_clusterName(TypedDict, closed=True):
    clusterName: "str"


class _RedshiftStorageProperties_workgroupName(TypedDict, closed=True):
    workgroupName: "str"


RedshiftStorageProperties: TypeAlias = (
    _RedshiftStorageProperties_clusterName | _RedshiftStorageProperties_workgroupName
)


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftStorageProperties) -> dict:
    if "clusterName" in value:
        return {"clusterName": value["clusterName"]}
    elif "workgroupName" in value:
        return {"workgroupName": value["workgroupName"]}
    else:
        raise SerializationError("RedshiftStorageProperties: no variant present")


def deserialize_json(data: dict) -> RedshiftStorageProperties:
    if "clusterName" in data:
        return {"clusterName": data["clusterName"]}
    elif "workgroupName" in data:
        return {"workgroupName": data["workgroupName"]}
    else:
        raise DeserializationError(
            "RedshiftStorageProperties: no recognized variant key"
        )
