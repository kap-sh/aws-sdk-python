"""Generated from Smithy shape ``com.amazonaws.wafv2#APIKeySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.api_key
    import aws_sdk_wafv2.types.api_key_version
    import aws_sdk_wafv2.types.timestamp
    import aws_sdk_wafv2.types.token_domains


class APIKeySummary(TypedDict):
    token_domains: NotRequired["aws_sdk_wafv2.types.token_domains.TokenDomains"]
    """<p>The token domains that are defined in this API key. </p>"""
    api_key: NotRequired["aws_sdk_wafv2.types.api_key.APIKey"]
    """<p>The generated, encrypted API key. You can copy this for use in your JavaScript CAPTCHA integration. </p>"""
    creation_timestamp: NotRequired["aws_sdk_wafv2.types.timestamp.Timestamp"]
    """<p>The date and time that the key was created. </p>"""
    version: "aws_sdk_wafv2.types.api_key_version.APIKeyVersion"
    """<p>Internal value used by WAF to manage the key. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: APIKeySummary) -> dict:
    out: dict = {}
    if "token_domains" in value:
        import aws_sdk_wafv2.types.token_domains

        out["TokenDomains"] = aws_sdk_wafv2.types.token_domains.serialize_aws_json_1_1(
            value["token_domains"]
        )
    if "api_key" in value:
        out["APIKey"] = value["api_key"]
    if "creation_timestamp" in value:
        import aws_sdk_wafv2.types.timestamp

        out["CreationTimestamp"] = aws_sdk_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["creation_timestamp"]
        )
    out["Version"] = value.get("version", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> APIKeySummary:
    out: APIKeySummary = {}  # type: ignore[typeddict-item]
    if "TokenDomains" in data:
        import aws_sdk_wafv2.types.token_domains

        out["token_domains"] = (
            aws_sdk_wafv2.types.token_domains.deserialize_aws_json_1_1(
                data["TokenDomains"]
            )
        )
    if "APIKey" in data:
        out["api_key"] = data["APIKey"]
    if "CreationTimestamp" in data:
        import aws_sdk_wafv2.types.timestamp

        out["creation_timestamp"] = (
            aws_sdk_wafv2.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    return out
