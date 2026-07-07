"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateNetworkResourceMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.network_resource_metadata_map
    import aws_sdk_networkmanager.types.resource_arn


class UpdateNetworkResourceMetadataRequest(TypedDict, closed=True):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    resource_arn: "aws_sdk_networkmanager.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource.</p>"""
    metadata: "aws_sdk_networkmanager.types.network_resource_metadata_map.NetworkResourceMetadataMap"
    """<p>The resource metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkResourceMetadataRequest) -> dict:
    out: dict = {}
    import aws_sdk_networkmanager.types.network_resource_metadata_map

    out["Metadata"] = (
        aws_sdk_networkmanager.types.network_resource_metadata_map.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateNetworkResourceMetadataRequest:
    out: UpdateNetworkResourceMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import aws_sdk_networkmanager.types.network_resource_metadata_map

        out["metadata"] = (
            aws_sdk_networkmanager.types.network_resource_metadata_map.deserialize_json(
                data["Metadata"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNetworkResourceMetadataRequest.metadata required"
        )
    return out
