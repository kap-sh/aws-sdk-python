"""Generated from Smithy shape ``com.amazonaws.wafv2#IPSetReferenceStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.ip_set_forwarded_ip_config
    import aws_sdk_wafv2.types.resource_arn


class IPSetReferenceStatement(TypedDict, closed=True):
    arn: "aws_sdk_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the <a>IPSet</a> that this statement references.</p>"""
    ip_set_forwarded_ip_config: NotRequired[
        "aws_sdk_wafv2.types.ip_set_forwarded_ip_config.IPSetForwardedIPConfig"
    ]
    """<p>The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name. </p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetReferenceStatement) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    if "ip_set_forwarded_ip_config" in value:
        import aws_sdk_wafv2.types.ip_set_forwarded_ip_config

        out["IPSetForwardedIPConfig"] = (
            aws_sdk_wafv2.types.ip_set_forwarded_ip_config.serialize_aws_json_1_1(
                value["ip_set_forwarded_ip_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSetReferenceStatement:
    out: IPSetReferenceStatement = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("IPSetReferenceStatement.arn required")
    if "IPSetForwardedIPConfig" in data:
        import aws_sdk_wafv2.types.ip_set_forwarded_ip_config

        out["ip_set_forwarded_ip_config"] = (
            aws_sdk_wafv2.types.ip_set_forwarded_ip_config.deserialize_aws_json_1_1(
                data["IPSetForwardedIPConfig"]
            )
        )
    return out
