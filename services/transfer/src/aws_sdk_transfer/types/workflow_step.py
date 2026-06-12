"""Generated from Smithy shape ``com.amazonaws.transfer#WorkflowStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.copy_step_details
    import aws_sdk_transfer.types.custom_step_details
    import aws_sdk_transfer.types.decrypt_step_details
    import aws_sdk_transfer.types.delete_step_details
    import aws_sdk_transfer.types.tag_step_details
    import aws_sdk_transfer.types.workflow_step_type


class WorkflowStep(TypedDict):
    type: NotRequired["aws_sdk_transfer.types.workflow_step_type.WorkflowStepType"]
    """<p> Currently, the following step types are supported. </p> <ul> <li> <p> <b> <code>COPY</code> </b> - Copy the file to another location.</p> </li> <li> <p> <b> <code>CUSTOM</code> </b> - Perform a custom step with an Lambda function target.</p> </li> <li> <p> <b> <code>DECRYPT</code> </b> - Decrypt a file that was encrypted before it was uploaded.</p> </li> <li> <p> <b> <code>DELETE</code> </b> - Delete the file.</p> </li> <li> <p> <b> <code>TAG</code> </b> - Add a tag to the file.</p> </li> </ul>"""
    copy_step_details: NotRequired[
        "aws_sdk_transfer.types.copy_step_details.CopyStepDetails"
    ]
    """<p>Details for a step that performs a file copy.</p> <p> Consists of the following values: </p> <ul> <li> <p>A description</p> </li> <li> <p>An Amazon S3 location for the destination of the file copy.</p> </li> <li> <p>A flag that indicates whether to overwrite an existing file of the same name. The default is <code>FALSE</code>.</p> </li> </ul>"""
    custom_step_details: NotRequired[
        "aws_sdk_transfer.types.custom_step_details.CustomStepDetails"
    ]
    """<p>Details for a step that invokes an Lambda function.</p> <p>Consists of the Lambda function's name, target, and timeout (in seconds). </p>"""
    delete_step_details: NotRequired[
        "aws_sdk_transfer.types.delete_step_details.DeleteStepDetails"
    ]
    """<p>Details for a step that deletes the file.</p>"""
    tag_step_details: NotRequired[
        "aws_sdk_transfer.types.tag_step_details.TagStepDetails"
    ]
    """<p>Details for a step that creates one or more tags.</p> <p>You specify one or more tags. Each tag contains a key-value pair.</p>"""
    decrypt_step_details: NotRequired[
        "aws_sdk_transfer.types.decrypt_step_details.DecryptStepDetails"
    ]
    """<p>Details for a step that decrypts an encrypted file.</p> <p>Consists of the following values:</p> <ul> <li> <p>A descriptive name</p> </li> <li> <p>An Amazon S3 or Amazon Elastic File System (Amazon EFS) location for the source file to decrypt.</p> </li> <li> <p>An S3 or Amazon EFS location for the destination of the file decryption.</p> </li> <li> <p>A flag that indicates whether to overwrite an existing file of the same name. The default is <code>FALSE</code>.</p> </li> <li> <p>The type of encryption that's used. Currently, only PGP encryption is supported.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowStep) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_transfer.types.workflow_step_type

        out["Type"] = aws_sdk_transfer.types.workflow_step_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "copy_step_details" in value:
        import aws_sdk_transfer.types.copy_step_details

        out["CopyStepDetails"] = (
            aws_sdk_transfer.types.copy_step_details.serialize_aws_json_1_1(
                value["copy_step_details"]
            )
        )
    if "custom_step_details" in value:
        import aws_sdk_transfer.types.custom_step_details

        out["CustomStepDetails"] = (
            aws_sdk_transfer.types.custom_step_details.serialize_aws_json_1_1(
                value["custom_step_details"]
            )
        )
    if "delete_step_details" in value:
        import aws_sdk_transfer.types.delete_step_details

        out["DeleteStepDetails"] = (
            aws_sdk_transfer.types.delete_step_details.serialize_aws_json_1_1(
                value["delete_step_details"]
            )
        )
    if "tag_step_details" in value:
        import aws_sdk_transfer.types.tag_step_details

        out["TagStepDetails"] = (
            aws_sdk_transfer.types.tag_step_details.serialize_aws_json_1_1(
                value["tag_step_details"]
            )
        )
    if "decrypt_step_details" in value:
        import aws_sdk_transfer.types.decrypt_step_details

        out["DecryptStepDetails"] = (
            aws_sdk_transfer.types.decrypt_step_details.serialize_aws_json_1_1(
                value["decrypt_step_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowStep:
    out: WorkflowStep = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_transfer.types.workflow_step_type

        out["type"] = (
            aws_sdk_transfer.types.workflow_step_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "CopyStepDetails" in data:
        import aws_sdk_transfer.types.copy_step_details

        out["copy_step_details"] = (
            aws_sdk_transfer.types.copy_step_details.deserialize_aws_json_1_1(
                data["CopyStepDetails"]
            )
        )
    if "CustomStepDetails" in data:
        import aws_sdk_transfer.types.custom_step_details

        out["custom_step_details"] = (
            aws_sdk_transfer.types.custom_step_details.deserialize_aws_json_1_1(
                data["CustomStepDetails"]
            )
        )
    if "DeleteStepDetails" in data:
        import aws_sdk_transfer.types.delete_step_details

        out["delete_step_details"] = (
            aws_sdk_transfer.types.delete_step_details.deserialize_aws_json_1_1(
                data["DeleteStepDetails"]
            )
        )
    if "TagStepDetails" in data:
        import aws_sdk_transfer.types.tag_step_details

        out["tag_step_details"] = (
            aws_sdk_transfer.types.tag_step_details.deserialize_aws_json_1_1(
                data["TagStepDetails"]
            )
        )
    if "DecryptStepDetails" in data:
        import aws_sdk_transfer.types.decrypt_step_details

        out["decrypt_step_details"] = (
            aws_sdk_transfer.types.decrypt_step_details.deserialize_aws_json_1_1(
                data["DecryptStepDetails"]
            )
        )
    return out
