"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeSourceLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DescribeSourceLocationRequest(TypedDict, closed=True):
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceLocationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSourceLocationRequest:
    out: DescribeSourceLocationRequest = {}  # type: ignore[typeddict-item]
    return out
