"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetInputFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_target_filter_path
    import aws_sdk_fis.types.experiment_template_target_filter_values


class ExperimentTemplateTargetInputFilter(TypedDict, closed=True):
    path: "aws_sdk_fis.types.experiment_template_target_filter_path.ExperimentTemplateTargetFilterPath"
    """<p>The attribute path for the filter.</p>"""
    values: "aws_sdk_fis.types.experiment_template_target_filter_values.ExperimentTemplateTargetFilterValues"
    """<p>The attribute values for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateTargetInputFilter) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import aws_sdk_fis.types.experiment_template_target_filter_values

    out["values"] = (
        aws_sdk_fis.types.experiment_template_target_filter_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExperimentTemplateTargetInputFilter:
    out: ExperimentTemplateTargetInputFilter = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("ExperimentTemplateTargetInputFilter.path required")
    if "values" in data:
        import aws_sdk_fis.types.experiment_template_target_filter_values

        out["values"] = (
            aws_sdk_fis.types.experiment_template_target_filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError(
            "ExperimentTemplateTargetInputFilter.values required"
        )
    return out
