"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfPortalProductSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.portal_product_summary

__listOfPortalProductSummary: TypeAlias = list[
    "capo_apigatewayv2.types.portal_product_summary.PortalProductSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPortalProductSummary) -> list:
    import capo_apigatewayv2.types.portal_product_summary

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.portal_product_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPortalProductSummary:
    import capo_apigatewayv2.types.portal_product_summary

    out: __listOfPortalProductSummary = []
    for item in data:
        out.append(
            capo_apigatewayv2.types.portal_product_summary.deserialize_json(item)
        )
    return out
