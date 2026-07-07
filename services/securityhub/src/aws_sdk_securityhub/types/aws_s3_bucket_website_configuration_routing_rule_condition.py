"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketWebsiteConfigurationRoutingRuleCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketWebsiteConfigurationRoutingRuleCondition(TypedDict, closed=True):
    http_error_code_returned_equals: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates to redirect the request if the HTTP error code matches this value.</p>"""
    key_prefix_equals: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates to redirect the request if the key prefix matches this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketWebsiteConfigurationRoutingRuleCondition) -> dict:
    out: dict = {}
    if "http_error_code_returned_equals" in value:
        out["HttpErrorCodeReturnedEquals"] = value["http_error_code_returned_equals"]
    if "key_prefix_equals" in value:
        out["KeyPrefixEquals"] = value["key_prefix_equals"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketWebsiteConfigurationRoutingRuleCondition:
    out: AwsS3BucketWebsiteConfigurationRoutingRuleCondition = {}  # type: ignore[typeddict-item]
    if "HttpErrorCodeReturnedEquals" in data:
        out["http_error_code_returned_equals"] = data["HttpErrorCodeReturnedEquals"]
    if "KeyPrefixEquals" in data:
        out["key_prefix_equals"] = data["KeyPrefixEquals"]
    return out
