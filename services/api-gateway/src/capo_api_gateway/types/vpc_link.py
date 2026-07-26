"""Generated from Smithy shape ``com.amazonaws.apigateway#VpcLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string
    import capo_api_gateway.types.vpc_link_status


class VpcLink(TypedDict, closed=True):
    id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.</p>"""
    name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name used to label and identify the VPC link.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the VPC link.</p>"""
    target_arns: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner.</p>"""
    status: NotRequired["capo_api_gateway.types.vpc_link_status.VpcLinkStatus"]
    """<p>The status of the VPC link. The valid values are <code>AVAILABLE</code>, <code>PENDING</code>, <code>DELETING</code>, or <code>FAILED</code>. Deploying an API will wait if the status is <code>PENDING</code> and will fail if the status is <code>DELETING</code>. </p>"""
    status_message: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A description about the VPC link status.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcLink) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "target_arns" in value:
        import capo_api_gateway.types.list_of_string

        out["targetArns"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["target_arns"]
        )
    if "status" in value:
        import capo_api_gateway.types.vpc_link_status

        out["status"] = capo_api_gateway.types.vpc_link_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> VpcLink:
    out: VpcLink = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "targetArns" in data:
        import capo_api_gateway.types.list_of_string

        out["target_arns"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["targetArns"]
        )
    if "status" in data:
        import capo_api_gateway.types.vpc_link_status

        out["status"] = capo_api_gateway.types.vpc_link_status.deserialize_json(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "tags" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    return out
