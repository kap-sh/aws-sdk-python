"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#DestinationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsecuretunneling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.service_list
    import aws_sdk_iotsecuretunneling.types.thing_name


class DestinationConfig(TypedDict):
    thing_name: NotRequired["aws_sdk_iotsecuretunneling.types.thing_name.ThingName"]
    """<p>The name of the IoT thing to which you want to connect.</p>"""
    services: "aws_sdk_iotsecuretunneling.types.service_list.ServiceList"
    """<p>A list of service names that identify the target application. The IoT client running on the destination device reads this value and uses it to look up a port or an IP address and a port. The IoT client instantiates the local proxy, which uses this information to connect to the destination application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationConfig) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    import aws_sdk_iotsecuretunneling.types.service_list

    out["services"] = (
        aws_sdk_iotsecuretunneling.types.service_list.serialize_aws_json_1_1(
            value["services"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationConfig:
    out: DestinationConfig = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "services" in data:
        import aws_sdk_iotsecuretunneling.types.service_list

        out["services"] = (
            aws_sdk_iotsecuretunneling.types.service_list.deserialize_aws_json_1_1(
                data["services"]
            )
        )
    else:
        raise DeserializationError("DestinationConfig.services required")
    return out
