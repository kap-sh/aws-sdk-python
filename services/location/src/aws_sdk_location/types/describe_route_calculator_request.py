"""Generated from Smithy shape ``com.amazonaws.location#DescribeRouteCalculatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name


class DescribeRouteCalculatorRequest(TypedDict, closed=True):
    calculator_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the route calculator resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRouteCalculatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRouteCalculatorRequest:
    out: DescribeRouteCalculatorRequest = {}  # type: ignore[typeddict-item]
    return out
