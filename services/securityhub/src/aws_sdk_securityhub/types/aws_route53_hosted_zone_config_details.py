"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53HostedZoneConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRoute53HostedZoneConfigDetails(TypedDict, closed=True):
    comment: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Any comments that you include about the hosted zone. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53HostedZoneConfigDetails) -> dict:
    out: dict = {}
    if "comment" in value:
        out["Comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> AwsRoute53HostedZoneConfigDetails:
    out: AwsRoute53HostedZoneConfigDetails = {}  # type: ignore[typeddict-item]
    if "Comment" in data:
        out["comment"] = data["Comment"]
    return out
