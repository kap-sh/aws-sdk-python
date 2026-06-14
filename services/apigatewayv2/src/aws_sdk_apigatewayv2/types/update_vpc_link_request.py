"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateVpcLinkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128


class UpdateVpcLinkRequest(TypedDict):
    name: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the VPC link.</p>"""
    vpc_link_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The ID of the VPC link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcLinkRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateVpcLinkRequest:
    out: UpdateVpcLinkRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
