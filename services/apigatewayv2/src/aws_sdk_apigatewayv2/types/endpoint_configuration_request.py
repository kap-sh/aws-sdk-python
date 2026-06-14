"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.acm_managed
    import aws_sdk_apigatewayv2.types.none


class EndpointConfigurationRequest(TypedDict):
    acm_managed: NotRequired["aws_sdk_apigatewayv2.types.acm_managed.ACMManaged"]
    """<p>Represents a domain name and certificate for a portal.</p>"""
    none: NotRequired["aws_sdk_apigatewayv2.types.none.None_"]
    """<p>Use the default portal domain name that is generated and managed by API Gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointConfigurationRequest) -> dict:
    out: dict = {}
    if "acm_managed" in value:
        import aws_sdk_apigatewayv2.types.acm_managed

        out["acmManaged"] = aws_sdk_apigatewayv2.types.acm_managed.serialize_json(
            value["acm_managed"]
        )
    if "none" in value:
        import aws_sdk_apigatewayv2.types.none

        out["none"] = aws_sdk_apigatewayv2.types.none.serialize_json(value["none"])
    return out


def deserialize_json(data: dict) -> EndpointConfigurationRequest:
    out: EndpointConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "acmManaged" in data:
        import aws_sdk_apigatewayv2.types.acm_managed

        out["acm_managed"] = aws_sdk_apigatewayv2.types.acm_managed.deserialize_json(
            data["acmManaged"]
        )
    if "none" in data:
        import aws_sdk_apigatewayv2.types.none

        out["none"] = aws_sdk_apigatewayv2.types.none.deserialize_json(data["none"])
    return out
