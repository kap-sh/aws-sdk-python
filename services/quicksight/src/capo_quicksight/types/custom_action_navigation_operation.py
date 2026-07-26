"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomActionNavigationOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.local_navigation_configuration


class CustomActionNavigationOperation(TypedDict, closed=True):
    local_navigation_configuration: NotRequired[
        "capo_quicksight.types.local_navigation_configuration.LocalNavigationConfiguration"
    ]
    """<p>The configuration that chooses the navigation target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionNavigationOperation) -> dict:
    out: dict = {}
    if "local_navigation_configuration" in value:
        import capo_quicksight.types.local_navigation_configuration

        out["LocalNavigationConfiguration"] = (
            capo_quicksight.types.local_navigation_configuration.serialize_json(
                value["local_navigation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomActionNavigationOperation:
    out: CustomActionNavigationOperation = {}  # type: ignore[typeddict-item]
    if "LocalNavigationConfiguration" in data:
        import capo_quicksight.types.local_navigation_configuration

        out["local_navigation_configuration"] = (
            capo_quicksight.types.local_navigation_configuration.deserialize_json(
                data["LocalNavigationConfiguration"]
            )
        )
    return out
