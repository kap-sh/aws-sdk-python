"""Generated from Smithy shape ``com.amazonaws.datazone#Region``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.parameter_store_path
    import capo_datazone.types.region_name


class _Region_regionName(TypedDict, closed=True):
    regionName: "capo_datazone.types.region_name.RegionName"


class _Region_regionNamePath(TypedDict, closed=True):
    regionNamePath: "capo_datazone.types.parameter_store_path.ParameterStorePath"


Region: TypeAlias = _Region_regionName | _Region_regionNamePath


# --- restJson1 ser/de ---
def serialize_json(value: Region) -> dict:
    if "regionName" in value:
        return {"regionName": value["regionName"]}
    elif "regionNamePath" in value:
        return {"regionNamePath": value["regionNamePath"]}
    else:
        raise SerializationError("Region: no variant present")


def deserialize_json(data: dict) -> Region:
    if "regionName" in data:
        return {"regionName": data["regionName"]}
    elif "regionNamePath" in data:
        return {"regionNamePath": data["regionNamePath"]}
    else:
        raise DeserializationError("Region: no recognized variant key")
