"""Generated from Smithy shape ``com.amazonaws.eks#DescribeUpdateResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.update


class DescribeUpdateResponse(TypedDict):
    update: NotRequired["aws_sdk_eks.types.update.Update"]
    """<p>The full description of the specified update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUpdateResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.serialize_json(value["update"])
    return out


def deserialize_json(data: dict) -> DescribeUpdateResponse:
    out: DescribeUpdateResponse = {}  # type: ignore[typeddict-item]
    if "update" in data:
        import aws_sdk_eks.types.update

        out["update"] = aws_sdk_eks.types.update.deserialize_json(data["update"])
    return out
