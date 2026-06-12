"""Generated from Smithy shape ``com.amazonaws.connectparticipant#DescribeViewResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.view


class DescribeViewResponse(TypedDict):
    view: NotRequired["aws_sdk_connectparticipant.types.view.View"]
    """<p>A view resource object. Contains metadata and content necessary to render the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeViewResponse) -> dict:
    out: dict = {}
    if "view" in value:
        import aws_sdk_connectparticipant.types.view

        out["View"] = aws_sdk_connectparticipant.types.view.serialize_json(
            value["view"]
        )
    return out


def deserialize_json(data: dict) -> DescribeViewResponse:
    out: DescribeViewResponse = {}  # type: ignore[typeddict-item]
    if "View" in data:
        import aws_sdk_connectparticipant.types.view

        out["view"] = aws_sdk_connectparticipant.types.view.deserialize_json(
            data["View"]
        )
    return out
