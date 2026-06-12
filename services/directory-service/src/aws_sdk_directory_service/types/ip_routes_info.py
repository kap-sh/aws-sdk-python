"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRoutesInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.ip_route_info

IpRoutesInfo: TypeAlias = list[
    "aws_sdk_directory_service.types.ip_route_info.IpRouteInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRoutesInfo) -> list:
    import aws_sdk_directory_service.types.ip_route_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.ip_route_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IpRoutesInfo:
    import aws_sdk_directory_service.types.ip_route_info

    out: IpRoutesInfo = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.ip_route_info.deserialize_aws_json_1_1(item)
        )
    return out
