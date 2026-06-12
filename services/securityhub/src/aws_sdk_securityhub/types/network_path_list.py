"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.network_path_component

NetworkPathList: TypeAlias = list[
    "aws_sdk_securityhub.types.network_path_component.NetworkPathComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPathList) -> list:
    import aws_sdk_securityhub.types.network_path_component

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.network_path_component.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkPathList:
    import aws_sdk_securityhub.types.network_path_component

    out: NetworkPathList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.network_path_component.deserialize_json(item)
        )
    return out
