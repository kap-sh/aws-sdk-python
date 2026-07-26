"""Generated from Smithy shape ``com.amazonaws.interconnect#Provider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_interconnect.types.cloud_service_provider
    import capo_interconnect.types.last_mile_provider


class _Provider_cloudServiceProvider(TypedDict, closed=True):
    cloudServiceProvider: (
        "capo_interconnect.types.cloud_service_provider.CloudServiceProvider"
    )


class _Provider_lastMileProvider(TypedDict, closed=True):
    lastMileProvider: "capo_interconnect.types.last_mile_provider.LastMileProvider"


Provider: TypeAlias = _Provider_cloudServiceProvider | _Provider_lastMileProvider


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Provider) -> dict:
    if "cloudServiceProvider" in value:
        return {"cloudServiceProvider": value["cloudServiceProvider"]}
    elif "lastMileProvider" in value:
        return {"lastMileProvider": value["lastMileProvider"]}
    else:
        raise SerializationError("Provider: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Provider:
    if "cloudServiceProvider" in data:
        return {"cloudServiceProvider": data["cloudServiceProvider"]}
    elif "lastMileProvider" in data:
        return {"lastMileProvider": data["lastMileProvider"]}
    else:
        raise DeserializationError("Provider: no recognized variant key")
