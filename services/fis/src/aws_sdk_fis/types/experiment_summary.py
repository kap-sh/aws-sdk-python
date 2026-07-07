"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.creation_time
    import aws_sdk_fis.types.experiment_id
    import aws_sdk_fis.types.experiment_options
    import aws_sdk_fis.types.experiment_state
    import aws_sdk_fis.types.experiment_template_id
    import aws_sdk_fis.types.resource_arn
    import aws_sdk_fis.types.tag_map


class ExperimentSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_fis.types.experiment_id.ExperimentId"]
    """<p>The ID of the experiment.</p>"""
    arn: NotRequired["aws_sdk_fis.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment.</p>"""
    experiment_template_id: NotRequired[
        "aws_sdk_fis.types.experiment_template_id.ExperimentTemplateId"
    ]
    """<p>The ID of the experiment template.</p>"""
    state: NotRequired["aws_sdk_fis.types.experiment_state.ExperimentState"]
    """<p>The state of the experiment.</p>"""
    creation_time: NotRequired["aws_sdk_fis.types.creation_time.CreationTime"]
    """<p>The time that the experiment was created.</p>"""
    tags: NotRequired["aws_sdk_fis.types.tag_map.TagMap"]
    """<p>The tags for the experiment.</p>"""
    experiment_options: NotRequired[
        "aws_sdk_fis.types.experiment_options.ExperimentOptions"
    ]
    """<p>The experiment options for the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "experiment_template_id" in value:
        out["experimentTemplateId"] = value["experiment_template_id"]
    if "state" in value:
        import aws_sdk_fis.types.experiment_state

        out["state"] = aws_sdk_fis.types.experiment_state.serialize_json(value["state"])
    if "creation_time" in value:
        import aws_sdk_fis.types.creation_time

        out["creationTime"] = aws_sdk_fis.types.creation_time.serialize_json(
            value["creation_time"]
        )
    if "tags" in value:
        import aws_sdk_fis.types.tag_map

        out["tags"] = aws_sdk_fis.types.tag_map.serialize_json(value["tags"])
    if "experiment_options" in value:
        import aws_sdk_fis.types.experiment_options

        out["experimentOptions"] = aws_sdk_fis.types.experiment_options.serialize_json(
            value["experiment_options"]
        )
    return out


def deserialize_json(data: dict) -> ExperimentSummary:
    out: ExperimentSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "experimentTemplateId" in data:
        out["experiment_template_id"] = data["experimentTemplateId"]
    if "state" in data:
        import aws_sdk_fis.types.experiment_state

        out["state"] = aws_sdk_fis.types.experiment_state.deserialize_json(
            data["state"]
        )
    if "creationTime" in data:
        import aws_sdk_fis.types.creation_time

        out["creation_time"] = aws_sdk_fis.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    if "tags" in data:
        import aws_sdk_fis.types.tag_map

        out["tags"] = aws_sdk_fis.types.tag_map.deserialize_json(data["tags"])
    if "experimentOptions" in data:
        import aws_sdk_fis.types.experiment_options

        out["experiment_options"] = (
            aws_sdk_fis.types.experiment_options.deserialize_json(
                data["experimentOptions"]
            )
        )
    return out
