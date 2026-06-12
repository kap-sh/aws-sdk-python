"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.access_endpoint

AccessEndpointList: TypeAlias = list[
    "aws_sdk_workspaces.types.access_endpoint.AccessEndpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessEndpointList) -> list:
    import aws_sdk_workspaces.types.access_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.access_endpoint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccessEndpointList:
    import aws_sdk_workspaces.types.access_endpoint

    out: AccessEndpointList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.access_endpoint.deserialize_aws_json_1_1(item)
        )
    return out
