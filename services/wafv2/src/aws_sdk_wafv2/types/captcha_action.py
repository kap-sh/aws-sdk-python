"""Generated from Smithy shape ``com.amazonaws.wafv2#CaptchaAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.custom_request_handling


class CaptchaAction(TypedDict):
    custom_request_handling: NotRequired[
        "aws_sdk_wafv2.types.custom_request_handling.CustomRequestHandling"
    ]
    r"""<p>Defines custom handling for the web request, used when the <code>CAPTCHA</code> inspection determines that the request's token is valid and unexpired.</p> <p>For information about customizing web requests and responses, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html\">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptchaAction) -> dict:
    out: dict = {}
    if "custom_request_handling" in value:
        import aws_sdk_wafv2.types.custom_request_handling

        out["CustomRequestHandling"] = (
            aws_sdk_wafv2.types.custom_request_handling.serialize_aws_json_1_1(
                value["custom_request_handling"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CaptchaAction:
    out: CaptchaAction = {}  # type: ignore[typeddict-item]
    if "CustomRequestHandling" in data:
        import aws_sdk_wafv2.types.custom_request_handling

        out["custom_request_handling"] = (
            aws_sdk_wafv2.types.custom_request_handling.deserialize_aws_json_1_1(
                data["CustomRequestHandling"]
            )
        )
    return out
