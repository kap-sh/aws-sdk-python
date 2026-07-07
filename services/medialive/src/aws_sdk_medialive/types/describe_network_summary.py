"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeNetworkSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__list_of_ip_pool
    import aws_sdk_medialive.types.__list_of_route
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.network_state


class DescribeNetworkSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of this Network. It is automatically assigned when the Network is created."""
    associated_cluster_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the Network. Unique in the AWS account. The ID is the resource-id portion of the ARN."""
    ip_pools: NotRequired["aws_sdk_medialive.types.__list_of_ip_pool.__listOfIpPool"]
    """An array of IpPools in your organization's network that identify a collection of IP addresses in your organization's network that are reserved for use in MediaLive Anywhere. MediaLive Anywhere uses these IP addresses for Push inputs (in both Bridge and NAT networks) and for output destinations (only in Bridge networks). Each IpPool specifies one CIDR block."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name that you specified for this Network."""
    routes: NotRequired["aws_sdk_medialive.types.__list_of_route.__listOfRoute"]
    """An array of routes that MediaLive Anywhere needs to know about in order to route encoding traffic."""
    state: NotRequired["aws_sdk_medialive.types.network_state.NetworkState"]
    """The current state of the Network. Only MediaLive Anywhere can change the state."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNetworkSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "associated_cluster_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["associatedClusterIds"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["associated_cluster_ids"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "ip_pools" in value:
        import aws_sdk_medialive.types.__list_of_ip_pool

        out["ipPools"] = aws_sdk_medialive.types.__list_of_ip_pool.serialize_json(
            value["ip_pools"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "routes" in value:
        import aws_sdk_medialive.types.__list_of_route

        out["routes"] = aws_sdk_medialive.types.__list_of_route.serialize_json(
            value["routes"]
        )
    if "state" in value:
        import aws_sdk_medialive.types.network_state

        out["state"] = aws_sdk_medialive.types.network_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> DescribeNetworkSummary:
    out: DescribeNetworkSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "associatedClusterIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["associated_cluster_ids"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["associatedClusterIds"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "ipPools" in data:
        import aws_sdk_medialive.types.__list_of_ip_pool

        out["ip_pools"] = aws_sdk_medialive.types.__list_of_ip_pool.deserialize_json(
            data["ipPools"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "routes" in data:
        import aws_sdk_medialive.types.__list_of_route

        out["routes"] = aws_sdk_medialive.types.__list_of_route.deserialize_json(
            data["routes"]
        )
    if "state" in data:
        import aws_sdk_medialive.types.network_state

        out["state"] = aws_sdk_medialive.types.network_state.deserialize_json(
            data["state"]
        )
    return out
