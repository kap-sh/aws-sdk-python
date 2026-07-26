"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTargetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_target_filter_path
    import capo_fis.types.experiment_target_filter_values


class ExperimentTargetFilter(TypedDict, closed=True):
    path: NotRequired[
        "capo_fis.types.experiment_target_filter_path.ExperimentTargetFilterPath"
    ]
    """<p>The attribute path for the filter.</p>"""
    values: NotRequired[
        "capo_fis.types.experiment_target_filter_values.ExperimentTargetFilterValues"
    ]
    """<p>The attribute values for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTargetFilter) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    if "values" in value:
        import capo_fis.types.experiment_target_filter_values

        out["values"] = capo_fis.types.experiment_target_filter_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> ExperimentTargetFilter:
    out: ExperimentTargetFilter = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    if "values" in data:
        import capo_fis.types.experiment_target_filter_values

        out["values"] = capo_fis.types.experiment_target_filter_values.deserialize_json(
            data["values"]
        )
    return out
