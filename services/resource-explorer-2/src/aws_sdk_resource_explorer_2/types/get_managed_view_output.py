"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetManagedViewOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.managed_view


class GetManagedViewOutput(TypedDict):
    managed_view: NotRequired[
        "aws_sdk_resource_explorer_2.types.managed_view.ManagedView"
    ]
    """<p>Details about the specified managed view. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedViewOutput) -> dict:
    out: dict = {}
    if "managed_view" in value:
        import aws_sdk_resource_explorer_2.types.managed_view

        out["ManagedView"] = (
            aws_sdk_resource_explorer_2.types.managed_view.serialize_json(
                value["managed_view"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetManagedViewOutput:
    out: GetManagedViewOutput = {}  # type: ignore[typeddict-item]
    if "ManagedView" in data:
        import aws_sdk_resource_explorer_2.types.managed_view

        out["managed_view"] = (
            aws_sdk_resource_explorer_2.types.managed_view.deserialize_json(
                data["ManagedView"]
            )
        )
    return out
