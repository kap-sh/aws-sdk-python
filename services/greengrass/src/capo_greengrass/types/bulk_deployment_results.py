"""Generated from Smithy shape ``com.amazonaws.greengrass#BulkDeploymentResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.bulk_deployment_result

BulkDeploymentResults: TypeAlias = list[
    "capo_greengrass.types.bulk_deployment_result.BulkDeploymentResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BulkDeploymentResults) -> list:
    import capo_greengrass.types.bulk_deployment_result

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.bulk_deployment_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> BulkDeploymentResults:
    import capo_greengrass.types.bulk_deployment_result

    out: BulkDeploymentResults = []
    for item in data:
        out.append(capo_greengrass.types.bulk_deployment_result.deserialize_json(item))
    return out
