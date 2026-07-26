"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfPortalSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.portal_summary

__listOfPortalSummary: TypeAlias = list[
    "capo_apigatewayv2.types.portal_summary.PortalSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPortalSummary) -> list:
    import capo_apigatewayv2.types.portal_summary

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.portal_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPortalSummary:
    import capo_apigatewayv2.types.portal_summary

    out: __listOfPortalSummary = []
    for item in data:
        out.append(capo_apigatewayv2.types.portal_summary.deserialize_json(item))
    return out
