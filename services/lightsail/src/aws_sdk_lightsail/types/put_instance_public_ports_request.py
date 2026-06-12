"""Generated from Smithy shape ``com.amazonaws.lightsail#PutInstancePublicPortsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.port_info_list
    import aws_sdk_lightsail.types.resource_name


class PutInstancePublicPortsRequest(TypedDict):
    port_infos: "aws_sdk_lightsail.types.port_info_list.PortInfoList"
    """<p>An array of objects to describe the ports to open for the specified instance.</p>"""
    instance_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance for which to open ports.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInstancePublicPortsRequest) -> dict:
    out: dict = {}
    import aws_sdk_lightsail.types.port_info_list

    out["portInfos"] = aws_sdk_lightsail.types.port_info_list.serialize_aws_json_1_1(
        value["port_infos"]
    )
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInstancePublicPortsRequest:
    out: PutInstancePublicPortsRequest = {}  # type: ignore[typeddict-item]
    if "portInfos" in data:
        import aws_sdk_lightsail.types.port_info_list

        out["port_infos"] = (
            aws_sdk_lightsail.types.port_info_list.deserialize_aws_json_1_1(
                data["portInfos"]
            )
        )
    else:
        raise DeserializationError("PutInstancePublicPortsRequest.port_infos required")
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError(
            "PutInstancePublicPortsRequest.instance_name required"
        )
    return out
