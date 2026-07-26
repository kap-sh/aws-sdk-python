"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketWebsiteConfigurationRedirectTo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsS3BucketWebsiteConfigurationRedirectTo(TypedDict, closed=True):
    hostname: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the host to redirect requests to.</p>"""
    protocol: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol to use when redirecting requests. By default, this field uses the same protocol as the original request. Valid values are <code>http</code> or <code>https</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketWebsiteConfigurationRedirectTo) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketWebsiteConfigurationRedirectTo:
    out: AwsS3BucketWebsiteConfigurationRedirectTo = {}  # type: ignore[typeddict-item]
    if "Hostname" in data:
        out["hostname"] = data["Hostname"]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    return out
