"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ResourceWarning``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_arc_region_switch.types.minimal_workflow
    import aws_sdk_arc_region_switch.types.resource_arn
    import aws_sdk_arc_region_switch.types.resource_warning_status
    import aws_sdk_arc_region_switch.types.step_name


class ResourceWarning(TypedDict):
    workflow: NotRequired[
        "aws_sdk_arc_region_switch.types.minimal_workflow.MinimalWorkflow"
    ]
    """<p>The workflow for the resource warning.</p>"""
    version: "str"
    """<p>The version for the resource warning.</p>"""
    step_name: NotRequired["aws_sdk_arc_region_switch.types.step_name.StepName"]
    """<p>The name of the step for the resource warning.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_arc_region_switch.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    warning_status: (
        "aws_sdk_arc_region_switch.types.resource_warning_status.ResourceWarningStatus"
    )
    """<p>The status of the resource warning.</p>"""
    warning_updated_time: "datetime.datetime"
    """<p>The timestamp when the warning was last updated.</p>"""
    warning_message: "str"
    """<p>The warning message about what needs to be corrected.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceWarning) -> dict:
    out: dict = {}
    if "workflow" in value:
        import aws_sdk_arc_region_switch.types.minimal_workflow

        out["workflow"] = (
            aws_sdk_arc_region_switch.types.minimal_workflow.serialize_aws_json_1_0(
                value["workflow"]
            )
        )
    out["version"] = value["version"]
    if "step_name" in value:
        out["stepName"] = value["step_name"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    import aws_sdk_arc_region_switch.types.resource_warning_status

    out["warningStatus"] = (
        aws_sdk_arc_region_switch.types.resource_warning_status.serialize_aws_json_1_0(
            value["warning_status"]
        )
    )
    import aws_sdk_arc_region_switch.types._prelude.timestamp

    out["warningUpdatedTime"] = (
        aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
            value["warning_updated_time"]
        )
    )
    out["warningMessage"] = value["warning_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceWarning:
    out: ResourceWarning = {}  # type: ignore[typeddict-item]
    if "workflow" in data:
        import aws_sdk_arc_region_switch.types.minimal_workflow

        out["workflow"] = (
            aws_sdk_arc_region_switch.types.minimal_workflow.deserialize_aws_json_1_0(
                data["workflow"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("ResourceWarning.version required")
    if "stepName" in data:
        out["step_name"] = data["stepName"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "warningStatus" in data:
        import aws_sdk_arc_region_switch.types.resource_warning_status

        out["warning_status"] = (
            aws_sdk_arc_region_switch.types.resource_warning_status.deserialize_aws_json_1_0(
                data["warningStatus"]
            )
        )
    else:
        raise DeserializationError("ResourceWarning.warning_status required")
    if "warningUpdatedTime" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["warning_updated_time"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["warningUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("ResourceWarning.warning_updated_time required")
    if "warningMessage" in data:
        out["warning_message"] = data["warningMessage"]
    else:
        raise DeserializationError("ResourceWarning.warning_message required")
    return out
