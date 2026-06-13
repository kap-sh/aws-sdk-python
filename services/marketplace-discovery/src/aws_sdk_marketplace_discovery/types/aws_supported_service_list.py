"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AwsSupportedServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.aws_supported_service

AwsSupportedServiceList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.aws_supported_service.AwsSupportedService"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsSupportedServiceList) -> list:
    import aws_sdk_marketplace_discovery.types.aws_supported_service

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.aws_supported_service.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsSupportedServiceList:
    import aws_sdk_marketplace_discovery.types.aws_supported_service

    out: AwsSupportedServiceList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.aws_supported_service.deserialize_json(
                item
            )
        )
    return out
