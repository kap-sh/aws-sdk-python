"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateVpcLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_string
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class CreateVpcLinkRequest(TypedDict, closed=True):
    name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name used to label and identify the VPC link.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the VPC link.</p>"""
    target_arns: "aws_sdk_api_gateway.types.list_of_string.ListOfString"
    """<p>The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner.</p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcLinkRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_api_gateway.types.list_of_string

    out["targetArns"] = aws_sdk_api_gateway.types.list_of_string.serialize_json(
        value["target_arns"]
    )
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
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
        import aws_sdk_api_gateway.types.list_of_string

        out["target_arns"] = aws_sdk_api_gateway.types.list_of_string.deserialize_json(
            data["targetArns"]
        )
    else:
        raise DeserializationError("CreateVpcLinkRequest.target_arns required")
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
