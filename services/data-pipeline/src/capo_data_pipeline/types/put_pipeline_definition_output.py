"""Generated from Smithy shape ``com.amazonaws.datapipeline#PutPipelineDefinitionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.boolean
    import capo_data_pipeline.types.validation_errors
    import capo_data_pipeline.types.validation_warnings


class PutPipelineDefinitionOutput(TypedDict, closed=True):
    validation_errors: NotRequired[
        "capo_data_pipeline.types.validation_errors.ValidationErrors"
    ]
    """<p>The validation errors that are associated with the objects defined in <code>pipelineObjects</code>.</p>"""
    validation_warnings: NotRequired[
        "capo_data_pipeline.types.validation_warnings.ValidationWarnings"
    ]
    """<p>The validation warnings that are associated with the objects defined in <code>pipelineObjects</code>.</p>"""
    errored: "capo_data_pipeline.types.boolean.boolean"
    """<p>Indicates whether there were validation errors, and the pipeline definition is stored but cannot be activated until you correct the pipeline and call <code>PutPipelineDefinition</code> to commit the corrected pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPipelineDefinitionOutput) -> dict:
    out: dict = {}
    if "validation_errors" in value:
        import capo_data_pipeline.types.validation_errors

        out["validationErrors"] = (
            capo_data_pipeline.types.validation_errors.serialize_aws_json_1_1(
                value["validation_errors"]
            )
        )
    if "validation_warnings" in value:
        import capo_data_pipeline.types.validation_warnings

        out["validationWarnings"] = (
            capo_data_pipeline.types.validation_warnings.serialize_aws_json_1_1(
                value["validation_warnings"]
            )
        )
    out["errored"] = value.get("errored", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPipelineDefinitionOutput:
    out: PutPipelineDefinitionOutput = {}  # type: ignore[typeddict-item]
    if "validationErrors" in data:
        import capo_data_pipeline.types.validation_errors

        out["validation_errors"] = (
            capo_data_pipeline.types.validation_errors.deserialize_aws_json_1_1(
                data["validationErrors"]
            )
        )
    if "validationWarnings" in data:
        import capo_data_pipeline.types.validation_warnings

        out["validation_warnings"] = (
            capo_data_pipeline.types.validation_warnings.deserialize_aws_json_1_1(
                data["validationWarnings"]
            )
        )
    if "errored" in data:
        out["errored"] = data["errored"]
    else:
        out["errored"] = False
    return out
