"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#UpdateViewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.view


class UpdateViewOutput(TypedDict, closed=True):
    view: NotRequired["aws_sdk_resource_explorer_2.types.view.View"]
    """<p>Details about the view that you changed with this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateViewOutput) -> dict:
    out: dict = {}
    if "view" in value:
        import aws_sdk_resource_explorer_2.types.view

        out["View"] = aws_sdk_resource_explorer_2.types.view.serialize_json(
            value["view"]
        )
    return out


def deserialize_json(data: dict) -> UpdateViewOutput:
    out: UpdateViewOutput = {}  # type: ignore[typeddict-item]
    if "View" in data:
        import aws_sdk_resource_explorer_2.types.view

        out["view"] = aws_sdk_resource_explorer_2.types.view.deserialize_json(
            data["View"]
        )
    return out
