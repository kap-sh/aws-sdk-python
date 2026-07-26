"""Generated from Smithy shape ``com.amazonaws.networkmanager#Peering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.aws_account_id
    import capo_networkmanager.types.core_network_arn
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.peering_error_list
    import capo_networkmanager.types.peering_id
    import capo_networkmanager.types.peering_state
    import capo_networkmanager.types.peering_type
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.tag_list


class Peering(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of the core network for the peering request.</p>"""
    core_network_arn: NotRequired[
        "capo_networkmanager.types.core_network_arn.CoreNetworkArn"
    ]
    """<p>The ARN of a core network.</p>"""
    peering_id: NotRequired["capo_networkmanager.types.peering_id.PeeringId"]
    """<p>The ID of the peering attachment. </p>"""
    owner_account_id: NotRequired[
        "capo_networkmanager.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the account owner.</p>"""
    peering_type: NotRequired["capo_networkmanager.types.peering_type.PeeringType"]
    """<p>The type of peering. This will be <code>TRANSIT_GATEWAY</code>.</p>"""
    state: NotRequired["capo_networkmanager.types.peering_state.PeeringState"]
    """<p>The current state of the peering connection. </p>"""
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The edge location for the peer.</p>"""
    resource_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The resource ARN of the peer.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the peering.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when the attachment peer was created.</p>"""
    last_modification_errors: NotRequired[
        "capo_networkmanager.types.peering_error_list.PeeringErrorList"
    ]
    """<p>Describes the error associated with the Connect peer request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Peering) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "core_network_arn" in value:
        out["CoreNetworkArn"] = value["core_network_arn"]
    if "peering_id" in value:
        out["PeeringId"] = value["peering_id"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "peering_type" in value:
        import capo_networkmanager.types.peering_type

        out["PeeringType"] = capo_networkmanager.types.peering_type.serialize_json(
            value["peering_type"]
        )
    if "state" in value:
        import capo_networkmanager.types.peering_state

        out["State"] = capo_networkmanager.types.peering_state.serialize_json(
            value["state"]
        )
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "last_modification_errors" in value:
        import capo_networkmanager.types.peering_error_list

        out["LastModificationErrors"] = (
            capo_networkmanager.types.peering_error_list.serialize_json(
                value["last_modification_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> Peering:
    out: Peering = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "CoreNetworkArn" in data:
        out["core_network_arn"] = data["CoreNetworkArn"]
    if "PeeringId" in data:
        out["peering_id"] = data["PeeringId"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "PeeringType" in data:
        import capo_networkmanager.types.peering_type

        out["peering_type"] = capo_networkmanager.types.peering_type.deserialize_json(
            data["PeeringType"]
        )
    if "State" in data:
        import capo_networkmanager.types.peering_state

        out["state"] = capo_networkmanager.types.peering_state.deserialize_json(
            data["State"]
        )
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "LastModificationErrors" in data:
        import capo_networkmanager.types.peering_error_list

        out["last_modification_errors"] = (
            capo_networkmanager.types.peering_error_list.deserialize_json(
                data["LastModificationErrors"]
            )
        )
    return out
