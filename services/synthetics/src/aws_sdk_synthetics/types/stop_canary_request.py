"""Generated from Smithy shape ``com.amazonaws.synthetics#StopCanaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary_name


class StopCanaryRequest(TypedDict):
    name: "aws_sdk_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want to stop. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">ListCanaries</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCanaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopCanaryRequest:
    out: StopCanaryRequest = {}  # type: ignore[typeddict-item]
    return out
