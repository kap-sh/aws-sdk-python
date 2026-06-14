"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Workflow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.version_number
    import aws_sdk_imagebuilder.types.workflow_build_version_arn
    import aws_sdk_imagebuilder.types.workflow_data
    import aws_sdk_imagebuilder.types.workflow_parameter_detail_list
    import aws_sdk_imagebuilder.types.workflow_state
    import aws_sdk_imagebuilder.types.workflow_type


class Workflow(TypedDict):
    arn: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the workflow resource.</p>"""
    version: NotRequired["aws_sdk_imagebuilder.types.version_number.VersionNumber"]
    """<p>The workflow resource version. Workflow resources are immutable. To make a change, you can clone a workflow or create a new version.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the workflow.</p>"""
    change_description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.</p>"""
    type: NotRequired["aws_sdk_imagebuilder.types.workflow_type.WorkflowType"]
    """<p>Specifies the image creation stage that the workflow applies to. Image Builder currently supports build and test workflows.</p>"""
    state: NotRequired["aws_sdk_imagebuilder.types.workflow_state.WorkflowState"]
    """<p>Describes the current status of the workflow and the reason for that status.</p>"""
    owner: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the workflow resource.</p>"""
    data: NotRequired["aws_sdk_imagebuilder.types.workflow_data.WorkflowData"]
    """<p>Contains the YAML document content for the workflow.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The KMS key identifier used to encrypt the workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The timestamp when Image Builder created the workflow resource.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that apply to the workflow resource</p>"""
    parameters: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_parameter_detail_list.WorkflowParameterDetailList"
    ]
    """<p>An array of input parameters that that the image workflow uses to control actions or configure settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Workflow) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    if "type" in value:
        import aws_sdk_imagebuilder.types.workflow_type

        out["type"] = aws_sdk_imagebuilder.types.workflow_type.serialize_json(
            value["type"]
        )
    if "state" in value:
        import aws_sdk_imagebuilder.types.workflow_state

        out["state"] = aws_sdk_imagebuilder.types.workflow_state.serialize_json(
            value["state"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "data" in value:
        out["data"] = value["data"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "parameters" in value:
        import aws_sdk_imagebuilder.types.workflow_parameter_detail_list

        out["parameters"] = (
            aws_sdk_imagebuilder.types.workflow_parameter_detail_list.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Workflow:
    out: Workflow = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "description" in data:
        out["description"] = data["description"]
    if "changeDescription" in data:
        out["change_description"] = data["changeDescription"]
    if "type" in data:
        import aws_sdk_imagebuilder.types.workflow_type

        out["type"] = aws_sdk_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    if "state" in data:
        import aws_sdk_imagebuilder.types.workflow_state

        out["state"] = aws_sdk_imagebuilder.types.workflow_state.deserialize_json(
            data["state"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "data" in data:
        out["data"] = data["data"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "parameters" in data:
        import aws_sdk_imagebuilder.types.workflow_parameter_detail_list

        out["parameters"] = (
            aws_sdk_imagebuilder.types.workflow_parameter_detail_list.deserialize_json(
                data["parameters"]
            )
        )
    return out
