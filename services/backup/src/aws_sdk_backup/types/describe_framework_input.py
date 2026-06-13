"""Generated from Smithy shape ``com.amazonaws.backup#DescribeFrameworkInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.framework_name


class DescribeFrameworkInput(TypedDict):
    framework_name: "aws_sdk_backup.types.framework_name.FrameworkName"
    """<p>The unique name of a framework.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFrameworkInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFrameworkInput:
    out: DescribeFrameworkInput = {}  # type: ignore[typeddict-item]
    return out
