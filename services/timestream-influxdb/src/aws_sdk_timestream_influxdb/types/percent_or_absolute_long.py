"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#PercentOrAbsoluteLong``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError, SerializationError


class _PercentOrAbsoluteLong_percent(TypedDict, closed=True):
    percent: "str"


class _PercentOrAbsoluteLong_absolute(TypedDict, closed=True):
    absolute: "int"


PercentOrAbsoluteLong: TypeAlias = (
    _PercentOrAbsoluteLong_percent | _PercentOrAbsoluteLong_absolute
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PercentOrAbsoluteLong) -> dict:
    if "percent" in value:
        return {"percent": value["percent"]}
    elif "absolute" in value:
        return {"absolute": value["absolute"]}
    else:
        raise SerializationError("PercentOrAbsoluteLong: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PercentOrAbsoluteLong:
    if "percent" in data:
        return {"percent": data["percent"]}
    elif "absolute" in data:
        return {"absolute": data["absolute"]}
    else:
        raise DeserializationError("PercentOrAbsoluteLong: no recognized variant key")
