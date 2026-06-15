"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2RulesActionCaptchaDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_custom_request_handling_details


class AwsWafv2RulesActionCaptchaDetails(TypedDict):
    custom_request_handling: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_custom_request_handling_details.AwsWafv2CustomRequestHandlingDetails"
    ]
    r"""<p> Defines custom handling for the web request, used when the CAPTCHA inspection determines that the request's token is valid and unexpired. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html\">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide.</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2RulesActionCaptchaDetails) -> dict:
    out: dict = {}
    if "custom_request_handling" in value:
        import aws_sdk_securityhub.types.aws_wafv2_custom_request_handling_details

        out["CustomRequestHandling"] = (
            aws_sdk_securityhub.types.aws_wafv2_custom_request_handling_details.serialize_json(
                value["custom_request_handling"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2RulesActionCaptchaDetails:
    out: AwsWafv2RulesActionCaptchaDetails = {}  # type: ignore[typeddict-item]
    if "CustomRequestHandling" in data:
        import aws_sdk_securityhub.types.aws_wafv2_custom_request_handling_details

        out["custom_request_handling"] = (
            aws_sdk_securityhub.types.aws_wafv2_custom_request_handling_details.deserialize_json(
                data["CustomRequestHandling"]
            )
        )
    return out
