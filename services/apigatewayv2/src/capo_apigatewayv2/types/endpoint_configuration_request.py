"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.acm_managed
    import capo_apigatewayv2.types.none


class EndpointConfigurationRequest(TypedDict, closed=True):
    acm_managed: NotRequired["capo_apigatewayv2.types.acm_managed.ACMManaged"]
    """<p>Represents a domain name and certificate for a portal.</p>"""
    none: NotRequired["capo_apigatewayv2.types.none.None_"]
    """<p>Use the default portal domain name that is generated and managed by API Gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointConfigurationRequest) -> dict:
    out: dict = {}
    if "acm_managed" in value:
        import capo_apigatewayv2.types.acm_managed

        out["acmManaged"] = capo_apigatewayv2.types.acm_managed.serialize_json(
            value["acm_managed"]
        )
    if "none" in value:
        import capo_apigatewayv2.types.none

        out["none"] = capo_apigatewayv2.types.none.serialize_json(value["none"])
    return out


def deserialize_json(data: dict) -> EndpointConfigurationRequest:
    out: EndpointConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "acmManaged" in data:
        import capo_apigatewayv2.types.acm_managed

        out["acm_managed"] = capo_apigatewayv2.types.acm_managed.deserialize_json(
            data["acmManaged"]
        )
    if "none" in data:
        import capo_apigatewayv2.types.none

        out["none"] = capo_apigatewayv2.types.none.deserialize_json(data["none"])
    return out
