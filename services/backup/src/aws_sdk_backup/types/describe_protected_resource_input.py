"""Generated from Smithy shape ``com.amazonaws.backup#DescribeProtectedResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn


class DescribeProtectedResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_backup.types.arn.ARN"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProtectedResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProtectedResourceInput:
    out: DescribeProtectedResourceInput = {}  # type: ignore[typeddict-item]
    return out
