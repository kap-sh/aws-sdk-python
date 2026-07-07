"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardFeatureConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.shared_view_configurations


class AnonymousUserDashboardFeatureConfigurations(TypedDict, closed=True):
    shared_view: NotRequired[
        "aws_sdk_quicksight.types.shared_view_configurations.SharedViewConfigurations"
    ]
    """<p>The shared view settings of an embedded dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnonymousUserDashboardFeatureConfigurations) -> dict:
    out: dict = {}
    if "shared_view" in value:
        import aws_sdk_quicksight.types.shared_view_configurations

        out["SharedView"] = (
            aws_sdk_quicksight.types.shared_view_configurations.serialize_json(
                value["shared_view"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnonymousUserDashboardFeatureConfigurations:
    out: AnonymousUserDashboardFeatureConfigurations = {}  # type: ignore[typeddict-item]
    if "SharedView" in data:
        import aws_sdk_quicksight.types.shared_view_configurations

        out["shared_view"] = (
            aws_sdk_quicksight.types.shared_view_configurations.deserialize_json(
                data["SharedView"]
            )
        )
    return out
