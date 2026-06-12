"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRoutes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.ip_route

IpRoutes: TypeAlias = list["aws_sdk_directory_service.types.ip_route.IpRoute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRoutes) -> list:
    import aws_sdk_directory_service.types.ip_route

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.ip_route.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IpRoutes:
    import aws_sdk_directory_service.types.ip_route

    out: IpRoutes = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.ip_route.deserialize_aws_json_1_1(item)
        )
    return out
