"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetRefreshProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.refresh_configuration
    import capo_quicksight.types.refresh_failure_configuration


class DataSetRefreshProperties(TypedDict, closed=True):
    refresh_configuration: NotRequired[
        "capo_quicksight.types.refresh_configuration.RefreshConfiguration"
    ]
    """<p>The refresh configuration for a dataset.</p>"""
    failure_configuration: NotRequired[
        "capo_quicksight.types.refresh_failure_configuration.RefreshFailureConfiguration"
    ]
    """<p>The failure configuration for a dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetRefreshProperties) -> dict:
    out: dict = {}
    if "refresh_configuration" in value:
        import capo_quicksight.types.refresh_configuration

        out["RefreshConfiguration"] = (
            capo_quicksight.types.refresh_configuration.serialize_json(
                value["refresh_configuration"]
            )
        )
    if "failure_configuration" in value:
        import capo_quicksight.types.refresh_failure_configuration

        out["FailureConfiguration"] = (
            capo_quicksight.types.refresh_failure_configuration.serialize_json(
                value["failure_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetRefreshProperties:
    out: DataSetRefreshProperties = {}  # type: ignore[typeddict-item]
    if "RefreshConfiguration" in data:
        import capo_quicksight.types.refresh_configuration

        out["refresh_configuration"] = (
            capo_quicksight.types.refresh_configuration.deserialize_json(
                data["RefreshConfiguration"]
            )
        )
    if "FailureConfiguration" in data:
        import capo_quicksight.types.refresh_failure_configuration

        out["failure_configuration"] = (
            capo_quicksight.types.refresh_failure_configuration.deserialize_json(
                data["FailureConfiguration"]
            )
        )
    return out
