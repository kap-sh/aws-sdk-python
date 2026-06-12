"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfPortalProductSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.portal_product_summary

__listOfPortalProductSummary: TypeAlias = list[
    "aws_sdk_apigatewayv2.types.portal_product_summary.PortalProductSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPortalProductSummary) -> list:
    import aws_sdk_apigatewayv2.types.portal_product_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_apigatewayv2.types.portal_product_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfPortalProductSummary:
    import aws_sdk_apigatewayv2.types.portal_product_summary

    out: __listOfPortalProductSummary = []
    for item in data:
        out.append(
            aws_sdk_apigatewayv2.types.portal_product_summary.deserialize_json(item)
        )
    return out
