"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeHubRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DescribeHubRequest(TypedDict, closed=True):
    hub_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the Hub resource to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHubRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeHubRequest:
    out: DescribeHubRequest = {}  # type: ignore[typeddict-item]
    return out
