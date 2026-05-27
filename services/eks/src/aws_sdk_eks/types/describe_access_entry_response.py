"""Generated from Smithy shape ``com.amazonaws.eks#DescribeAccessEntryResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.access_entry


class DescribeAccessEntryResponse(TypedDict):
    access_entry: NotRequired["aws_sdk_eks.types.access_entry.AccessEntry"]
    """<p>Information about the access entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessEntryResponse) -> dict:
    out: dict = {}
    if "access_entry" in value:
        import aws_sdk_eks.types.access_entry

        out["accessEntry"] = aws_sdk_eks.types.access_entry.serialize_json(
            value["access_entry"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAccessEntryResponse:
    out: DescribeAccessEntryResponse = {}  # type: ignore[typeddict-item]
    if "accessEntry" in data:
        import aws_sdk_eks.types.access_entry

        out["access_entry"] = aws_sdk_eks.types.access_entry.deserialize_json(
            data["accessEntry"]
        )
    return out
