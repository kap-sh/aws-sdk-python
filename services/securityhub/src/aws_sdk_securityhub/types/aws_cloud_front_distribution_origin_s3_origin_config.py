"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginS3OriginConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsCloudFrontDistributionOriginS3OriginConfig(TypedDict, closed=True):
    origin_access_identity: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The CloudFront origin access identity to associate with the origin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginS3OriginConfig) -> dict:
    out: dict = {}
    if "origin_access_identity" in value:
        out["OriginAccessIdentity"] = value["origin_access_identity"]
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginS3OriginConfig:
    out: AwsCloudFrontDistributionOriginS3OriginConfig = {}  # type: ignore[typeddict-item]
    if "OriginAccessIdentity" in data:
        out["origin_access_identity"] = data["OriginAccessIdentity"]
    return out
