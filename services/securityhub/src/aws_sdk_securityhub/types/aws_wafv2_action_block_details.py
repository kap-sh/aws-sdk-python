"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2ActionBlockDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_custom_response_details


class AwsWafv2ActionBlockDetails(TypedDict):
    custom_response: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_custom_response_details.AwsWafv2CustomResponseDetails"
    ]
    """<p> Defines a custom response for the web request. For information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html\">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide.</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2ActionBlockDetails) -> dict:
    out: dict = {}
    if "custom_response" in value:
        import aws_sdk_securityhub.types.aws_wafv2_custom_response_details

        out["CustomResponse"] = (
            aws_sdk_securityhub.types.aws_wafv2_custom_response_details.serialize_json(
                value["custom_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2ActionBlockDetails:
    out: AwsWafv2ActionBlockDetails = {}  # type: ignore[typeddict-item]
    if "CustomResponse" in data:
        import aws_sdk_securityhub.types.aws_wafv2_custom_response_details

        out["custom_response"] = (
            aws_sdk_securityhub.types.aws_wafv2_custom_response_details.deserialize_json(
                data["CustomResponse"]
            )
        )
    return out
