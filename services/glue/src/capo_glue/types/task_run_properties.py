"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.export_labels_task_run_properties
    import capo_glue.types.find_matches_task_run_properties
    import capo_glue.types.import_labels_task_run_properties
    import capo_glue.types.labeling_set_generation_task_run_properties
    import capo_glue.types.task_type


class TaskRunProperties(TypedDict, closed=True):
    task_type: NotRequired["capo_glue.types.task_type.TaskType"]
    """<p>The type of task run.</p>"""
    import_labels_task_run_properties: NotRequired[
        "capo_glue.types.import_labels_task_run_properties.ImportLabelsTaskRunProperties"
    ]
    """<p>The configuration properties for an importing labels task run.</p>"""
    export_labels_task_run_properties: NotRequired[
        "capo_glue.types.export_labels_task_run_properties.ExportLabelsTaskRunProperties"
    ]
    """<p>The configuration properties for an exporting labels task run.</p>"""
    labeling_set_generation_task_run_properties: NotRequired[
        "capo_glue.types.labeling_set_generation_task_run_properties.LabelingSetGenerationTaskRunProperties"
    ]
    """<p>The configuration properties for a labeling set generation task run.</p>"""
    find_matches_task_run_properties: NotRequired[
        "capo_glue.types.find_matches_task_run_properties.FindMatchesTaskRunProperties"
    ]
    """<p>The configuration properties for a find matches task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunProperties) -> dict:
    out: dict = {}
    if "task_type" in value:
        import capo_glue.types.task_type

        out["TaskType"] = capo_glue.types.task_type.serialize_aws_json_1_1(
            value["task_type"]
        )
    if "import_labels_task_run_properties" in value:
        import capo_glue.types.import_labels_task_run_properties

        out["ImportLabelsTaskRunProperties"] = (
            capo_glue.types.import_labels_task_run_properties.serialize_aws_json_1_1(
                value["import_labels_task_run_properties"]
            )
        )
    if "export_labels_task_run_properties" in value:
        import capo_glue.types.export_labels_task_run_properties

        out["ExportLabelsTaskRunProperties"] = (
            capo_glue.types.export_labels_task_run_properties.serialize_aws_json_1_1(
                value["export_labels_task_run_properties"]
            )
        )
    if "labeling_set_generation_task_run_properties" in value:
        import capo_glue.types.labeling_set_generation_task_run_properties

        out["LabelingSetGenerationTaskRunProperties"] = (
            capo_glue.types.labeling_set_generation_task_run_properties.serialize_aws_json_1_1(
                value["labeling_set_generation_task_run_properties"]
            )
        )
    if "find_matches_task_run_properties" in value:
        import capo_glue.types.find_matches_task_run_properties

        out["FindMatchesTaskRunProperties"] = (
            capo_glue.types.find_matches_task_run_properties.serialize_aws_json_1_1(
                value["find_matches_task_run_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskRunProperties:
    out: TaskRunProperties = {}  # type: ignore[typeddict-item]
    if "TaskType" in data:
        import capo_glue.types.task_type

        out["task_type"] = capo_glue.types.task_type.deserialize_aws_json_1_1(
            data["TaskType"]
        )
    if "ImportLabelsTaskRunProperties" in data:
        import capo_glue.types.import_labels_task_run_properties

        out["import_labels_task_run_properties"] = (
            capo_glue.types.import_labels_task_run_properties.deserialize_aws_json_1_1(
                data["ImportLabelsTaskRunProperties"]
            )
        )
    if "ExportLabelsTaskRunProperties" in data:
        import capo_glue.types.export_labels_task_run_properties

        out["export_labels_task_run_properties"] = (
            capo_glue.types.export_labels_task_run_properties.deserialize_aws_json_1_1(
                data["ExportLabelsTaskRunProperties"]
            )
        )
    if "LabelingSetGenerationTaskRunProperties" in data:
        import capo_glue.types.labeling_set_generation_task_run_properties

        out["labeling_set_generation_task_run_properties"] = (
            capo_glue.types.labeling_set_generation_task_run_properties.deserialize_aws_json_1_1(
                data["LabelingSetGenerationTaskRunProperties"]
            )
        )
    if "FindMatchesTaskRunProperties" in data:
        import capo_glue.types.find_matches_task_run_properties

        out["find_matches_task_run_properties"] = (
            capo_glue.types.find_matches_task_run_properties.deserialize_aws_json_1_1(
                data["FindMatchesTaskRunProperties"]
            )
        )
    return out
