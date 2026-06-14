"""Generated from Smithy shape ``com.amazonaws.synthetics#StartCanaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary_name


class StartCanaryRequest(TypedDict):
    name: "aws_sdk_synthetics.types.canary_name.CanaryName"
    r"""<p>The name of the canary that you want to run. To find canary names, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCanaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartCanaryRequest:
    out: StartCanaryRequest = {}  # type: ignore[typeddict-item]
    return out
