"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateNetworkResourceMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_resource_metadata_map
    import aws_sdk_networkmanager.types.resource_arn


class UpdateNetworkResourceMetadataResponse(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource.</p>"""
    metadata: NotRequired[
        "aws_sdk_networkmanager.types.network_resource_metadata_map.NetworkResourceMetadataMap"
    ]
    """<p>The updated resource metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkResourceMetadataResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "metadata" in value:
        import aws_sdk_networkmanager.types.network_resource_metadata_map

        out["Metadata"] = (
            aws_sdk_networkmanager.types.network_resource_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkResourceMetadataResponse:
    out: UpdateNetworkResourceMetadataResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Metadata" in data:
        import aws_sdk_networkmanager.types.network_resource_metadata_map

        out["metadata"] = (
            aws_sdk_networkmanager.types.network_resource_metadata_map.deserialize_json(
                data["Metadata"]
            )
        )
    return out
