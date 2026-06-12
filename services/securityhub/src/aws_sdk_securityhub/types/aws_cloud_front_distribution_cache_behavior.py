"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionCacheBehavior``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsCloudFrontDistributionCacheBehavior(TypedDict):
    viewer_protocol_policy: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The protocol that viewers can use to access the files in an origin. You can specify the following options:</p> <ul> <li> <p> <code>allow-all</code> - Viewers can use HTTP or HTTPS.</p> </li> <li> <p> <code>redirect-to-https</code> - CloudFront responds to HTTP requests with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL. The viewer then uses the new URL to resubmit.</p> </li> <li> <p> <code>https-only</code> - CloudFront responds to HTTP request with an HTTP status code of 403 (Forbidden).</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionCacheBehavior) -> dict:
    out: dict = {}
    if "viewer_protocol_policy" in value:
        out["ViewerProtocolPolicy"] = value["viewer_protocol_policy"]
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionCacheBehavior:
    out: AwsCloudFrontDistributionCacheBehavior = {}  # type: ignore[typeddict-item]
    if "ViewerProtocolPolicy" in data:
        out["viewer_protocol_policy"] = data["ViewerProtocolPolicy"]
    return out
