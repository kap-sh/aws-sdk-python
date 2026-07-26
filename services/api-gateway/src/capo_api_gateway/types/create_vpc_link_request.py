"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateVpcLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class CreateVpcLinkRequest(TypedDict, closed=True):
    name: "capo_api_gateway.types.string.String"
    """<p>The name used to label and identify the VPC link.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the VPC link.</p>"""
    target_arns: "capo_api_gateway.types.list_of_string.ListOfString"
    """<p>The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcLinkRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_api_gateway.types.list_of_string

    out["targetArns"] = capo_api_gateway.types.list_of_string.serialize_json(
        value["target_arns"]
    )
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateVpcLinkRequest:
    out: CreateVpcLinkRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateVpcLinkRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "targetArns" in data:
        import capo_api_gateway.types.list_of_string

        out["target_arns"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["targetArns"]
        )
    else:
        raise DeserializationError("CreateVpcLinkRequest.target_arns required")
    if "tags" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    return out
