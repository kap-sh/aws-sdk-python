"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.version_number
    import aws_sdk_imagebuilder.types.workflow_type
    import aws_sdk_imagebuilder.types.workflow_version_arn


class WorkflowVersion(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_version_arn.WorkflowVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the workflow.</p>"""
    version: NotRequired["aws_sdk_imagebuilder.types.version_number.VersionNumber"]
    """<p>The semantic version of the workflow resource. The format includes three nodes: <major>.<minor>.<patch>.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes the workflow.</p>"""
    type: NotRequired["aws_sdk_imagebuilder.types.workflow_type.WorkflowType"]
    """<p>The image creation stage that this workflow applies to. Image Builder currently supports build and test stage workflows.</p>"""
    owner: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the workflow resource.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when Image Builder created the workflow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowVersion) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import aws_sdk_imagebuilder.types.workflow_type

        out["type"] = aws_sdk_imagebuilder.types.workflow_type.serialize_json(
            value["type"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    return out


def deserialize_json(data: dict) -> WorkflowVersion:
    out: WorkflowVersion = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_imagebuilder.types.workflow_type

        out["type"] = aws_sdk_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    return out
