"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessEndpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.access_endpoint_list
    import aws_sdk_workspaces.types.internet_fallback_protocol_list


class AccessEndpointConfig(TypedDict, closed=True):
    access_endpoints: "aws_sdk_workspaces.types.access_endpoint_list.AccessEndpointList"
    """<p>Indicates a list of access endpoints associated with this directory.</p>"""
    internet_fallback_protocols: NotRequired[
        "aws_sdk_workspaces.types.internet_fallback_protocol_list.InternetFallbackProtocolList"
    ]
    """<p>Indicates a list of protocols that fallback to using the public Internet when streaming over a VPC endpoint is not available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessEndpointConfig) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.access_endpoint_list

    out["AccessEndpoints"] = (
        aws_sdk_workspaces.types.access_endpoint_list.serialize_aws_json_1_1(
            value["access_endpoints"]
        )
    )
    if "internet_fallback_protocols" in value:
        import aws_sdk_workspaces.types.internet_fallback_protocol_list

        out["InternetFallbackProtocols"] = (
            aws_sdk_workspaces.types.internet_fallback_protocol_list.serialize_aws_json_1_1(
                value["internet_fallback_protocols"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessEndpointConfig:
    out: AccessEndpointConfig = {}  # type: ignore[typeddict-item]
    if "AccessEndpoints" in data:
        import aws_sdk_workspaces.types.access_endpoint_list

        out["access_endpoints"] = (
            aws_sdk_workspaces.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    else:
        raise DeserializationError("AccessEndpointConfig.access_endpoints required")
    if "InternetFallbackProtocols" in data:
        import aws_sdk_workspaces.types.internet_fallback_protocol_list

        out["internet_fallback_protocols"] = (
            aws_sdk_workspaces.types.internet_fallback_protocol_list.deserialize_aws_json_1_1(
                data["InternetFallbackProtocols"]
            )
        )
    return out
