"""Generated from Smithy shape ``com.amazonaws.connect#DescribeViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.view


class DescribeViewResponse(TypedDict, closed=True):
    view: NotRequired["aws_sdk_connect.types.view.View"]
    """<p>All view data is contained within the View object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeViewResponse) -> dict:
    out: dict = {}
    if "view" in value:
        import aws_sdk_connect.types.view

        out["View"] = aws_sdk_connect.types.view.serialize_json(value["view"])
    return out


def deserialize_json(data: dict) -> DescribeViewResponse:
    out: DescribeViewResponse = {}  # type: ignore[typeddict-item]
    if "View" in data:
        import aws_sdk_connect.types.view

        out["view"] = aws_sdk_connect.types.view.deserialize_json(data["View"])
    return out
