"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_target_filter_path
    import aws_sdk_fis.types.experiment_template_target_filter_values


class ExperimentTemplateTargetFilter(TypedDict, closed=True):
    path: NotRequired[
        "aws_sdk_fis.types.experiment_template_target_filter_path.ExperimentTemplateTargetFilterPath"
    ]
    """<p>The attribute path for the filter.</p>"""
    values: NotRequired[
        "aws_sdk_fis.types.experiment_template_target_filter_values.ExperimentTemplateTargetFilterValues"
    ]
    """<p>The attribute values for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateTargetFilter) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    if "values" in value:
        import aws_sdk_fis.types.experiment_template_target_filter_values

        out["values"] = (
            aws_sdk_fis.types.experiment_template_target_filter_values.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentTemplateTargetFilter:
    out: ExperimentTemplateTargetFilter = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    if "values" in data:
        import aws_sdk_fis.types.experiment_template_target_filter_values

        out["values"] = (
            aws_sdk_fis.types.experiment_template_target_filter_values.deserialize_json(
                data["values"]
            )
        )
    return out
