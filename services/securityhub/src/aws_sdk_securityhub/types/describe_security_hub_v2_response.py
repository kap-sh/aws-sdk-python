"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeSecurityHubV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DescribeSecurityHubV2Response(TypedDict):
    hub_v2_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the service resource.</p>"""
    subscribed_at: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The date and time when the service was enabled in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityHubV2Response) -> dict:
    out: dict = {}
    if "hub_v2_arn" in value:
        out["HubV2Arn"] = value["hub_v2_arn"]
    if "subscribed_at" in value:
        out["SubscribedAt"] = value["subscribed_at"]
    return out


def deserialize_json(data: dict) -> DescribeSecurityHubV2Response:
    out: DescribeSecurityHubV2Response = {}  # type: ignore[typeddict-item]
    if "HubV2Arn" in data:
        out["hub_v2_arn"] = data["HubV2Arn"]
    if "SubscribedAt" in data:
        out["subscribed_at"] = data["SubscribedAt"]
    return out
