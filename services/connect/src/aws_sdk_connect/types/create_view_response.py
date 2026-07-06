"""Generated from Smithy shape ``com.amazonaws.connect#CreateViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.view


class CreateViewResponse(TypedDict, closed=True):
    view: NotRequired["aws_sdk_connect.types.view.View"]
    """<p>A view resource object. Contains metadata and content necessary to render the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateViewResponse) -> dict:
    out: dict = {}
    if "view" in value:
        import aws_sdk_connect.types.view

        out["View"] = aws_sdk_connect.types.view.serialize_json(value["view"])
    return out


def deserialize_json(data: dict) -> CreateViewResponse:
    out: CreateViewResponse = {}  # type: ignore[typeddict-item]
    if "View" in data:
        import aws_sdk_connect.types.view

        out["view"] = aws_sdk_connect.types.view.deserialize_json(data["View"])
    return out
