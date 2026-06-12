"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Section``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__string


class Section(TypedDict):
    product_rest_endpoint_page_arns: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
    ]
    """<p>The ARNs of the product REST endpoint pages in a portal product.</p>"""
    section_name: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The section name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Section) -> dict:
    out: dict = {}
    if "product_rest_endpoint_page_arns" in value:
        import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048

        out["productRestEndpointPageArns"] = (
            aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.serialize_json(
                value["product_rest_endpoint_page_arns"]
            )
        )
    if "section_name" in value:
        out["sectionName"] = value["section_name"]
    return out


def deserialize_json(data: dict) -> Section:
    out: Section = {}  # type: ignore[typeddict-item]
    if "productRestEndpointPageArns" in data:
        import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048

        out["product_rest_endpoint_page_arns"] = (
            aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.deserialize_json(
                data["productRestEndpointPageArns"]
            )
        )
    if "sectionName" in data:
        out["section_name"] = data["sectionName"]
    return out
