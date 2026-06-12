"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignHook``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.mode


class CampaignHook(TypedDict):
    lambda_function_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign.</p>"""
    mode: NotRequired["aws_sdk_pinpoint.types.mode.Mode"]
    """<p>The mode that Amazon Pinpoint uses to invoke the AWS Lambda function. Possible values are:</p> <ul><li><p>FILTER - Invoke the function to customize the segment that's used by a campaign.</p></li> <li><p>DELIVERY - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the CustomDeliveryConfiguration and CampaignCustomMessage objects of the campaign.</p></li></ul>"""
    web_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The web URL that Amazon Pinpoint calls to invoke the AWS Lambda function over HTTPS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignHook) -> dict:
    out: dict = {}
    if "lambda_function_name" in value:
        out["LambdaFunctionName"] = value["lambda_function_name"]
    if "mode" in value:
        import aws_sdk_pinpoint.types.mode

        out["Mode"] = aws_sdk_pinpoint.types.mode.serialize_json(value["mode"])
    if "web_url" in value:
        out["WebUrl"] = value["web_url"]
    return out


def deserialize_json(data: dict) -> CampaignHook:
    out: CampaignHook = {}  # type: ignore[typeddict-item]
    if "LambdaFunctionName" in data:
        out["lambda_function_name"] = data["LambdaFunctionName"]
    if "Mode" in data:
        import aws_sdk_pinpoint.types.mode

        out["mode"] = aws_sdk_pinpoint.types.mode.deserialize_json(data["Mode"])
    if "WebUrl" in data:
        out["web_url"] = data["WebUrl"]
    return out
