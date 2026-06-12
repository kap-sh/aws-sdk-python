"""Generated from Smithy shape ``com.amazonaws.greengrass#BulkDeployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.bulk_deployment

BulkDeployments: TypeAlias = list[
    "aws_sdk_greengrass.types.bulk_deployment.BulkDeployment"
]


# --- restJson1 ser/de ---
def serialize_json(value: BulkDeployments) -> list:
    import aws_sdk_greengrass.types.bulk_deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.bulk_deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> BulkDeployments:
    import aws_sdk_greengrass.types.bulk_deployment

    out: BulkDeployments = []
    for item in data:
        out.append(aws_sdk_greengrass.types.bulk_deployment.deserialize_json(item))
    return out
