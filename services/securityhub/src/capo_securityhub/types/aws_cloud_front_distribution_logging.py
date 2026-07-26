"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionLogging``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsCloudFrontDistributionLogging(TypedDict, closed=True):
    bucket: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The S3 bucket to store the access logs in.</p>"""
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>With this field, you can enable or disable the selected distribution.</p>"""
    include_cookies: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether you want CloudFront to include cookies in access logs.</p>"""
    prefix: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An optional string that you want CloudFront to use as a prefix to the access log filenames for this distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionLogging) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "include_cookies" in value:
        out["IncludeCookies"] = value["include_cookies"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionLogging:
    out: AwsCloudFrontDistributionLogging = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "IncludeCookies" in data:
        out["include_cookies"] = data["IncludeCookies"]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    return out
