"""Generated from Smithy shape ``com.amazonaws.lakeformation#DescribeResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.resource_arn_string


class DescribeResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The resource ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DescribeResourceRequest:
    out: DescribeResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DescribeResourceRequest.resource_arn required")
    return out
