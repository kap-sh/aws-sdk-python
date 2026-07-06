"""Generated from Smithy shape ``com.amazonaws.connect#DescribeQuickConnectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.quick_connect


class DescribeQuickConnectResponse(TypedDict, closed=True):
    quick_connect: NotRequired["aws_sdk_connect.types.quick_connect.QuickConnect"]
    """<p>Information about the quick connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQuickConnectResponse) -> dict:
    out: dict = {}
    if "quick_connect" in value:
        import aws_sdk_connect.types.quick_connect

        out["QuickConnect"] = aws_sdk_connect.types.quick_connect.serialize_json(
            value["quick_connect"]
        )
    return out


def deserialize_json(data: dict) -> DescribeQuickConnectResponse:
    out: DescribeQuickConnectResponse = {}  # type: ignore[typeddict-item]
    if "QuickConnect" in data:
        import aws_sdk_connect.types.quick_connect

        out["quick_connect"] = aws_sdk_connect.types.quick_connect.deserialize_json(
            data["QuickConnect"]
        )
    return out
