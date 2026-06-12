"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.logical_resource_id
    import aws_sdk_cloudformation.types.module_info
    import aws_sdk_cloudformation.types.physical_resource_id
    import aws_sdk_cloudformation.types.resource_status
    import aws_sdk_cloudformation.types.resource_status_reason
    import aws_sdk_cloudformation.types.resource_type
    import aws_sdk_cloudformation.types.stack_resource_drift_information_summary
    import aws_sdk_cloudformation.types.timestamp


class StackResourceSummary(TypedDict):
    logical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource specified in the template.</p>"""
    physical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The name or unique identifier that corresponds to a physical instance ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_cloudformation.types.resource_type.ResourceType"
    ]
    """<p>Type of resource. (For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html\">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>.)</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_cloudformation.types.timestamp.Timestamp"
    ]
    """<p>Time the status was updated.</p>"""
    resource_status: NotRequired[
        "aws_sdk_cloudformation.types.resource_status.ResourceStatus"
    ]
    """<p>Current status of the resource.</p>"""
    resource_status_reason: NotRequired[
        "aws_sdk_cloudformation.types.resource_status_reason.ResourceStatusReason"
    ]
    """<p>Success/failure message associated with the resource.</p>"""
    drift_information: NotRequired[
        "aws_sdk_cloudformation.types.stack_resource_drift_information_summary.StackResourceDriftInformationSummary"
    ]
    """<p>Information about whether the resource's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\">Detect unmanaged configuration changes to stacks and resources with drift detection</a>.</p>"""
    module_info: NotRequired["aws_sdk_cloudformation.types.module_info.ModuleInfo"]
    """<p>Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))
    if "physical_resource_id" in value:
        pairs.append(
            (f"{prefix}.PhysicalResourceId", str(value["physical_resource_id"]))
        )
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "last_updated_timestamp" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["last_updated_timestamp"], pairs, f"{prefix}.LastUpdatedTimestamp"
        )
    if "resource_status" in value:
        import aws_sdk_cloudformation.types.resource_status

        aws_sdk_cloudformation.types.resource_status.serialize_query(
            value["resource_status"], pairs, f"{prefix}.ResourceStatus"
        )
    if "resource_status_reason" in value:
        pairs.append(
            (f"{prefix}.ResourceStatusReason", str(value["resource_status_reason"]))
        )
    if "drift_information" in value:
        import aws_sdk_cloudformation.types.stack_resource_drift_information_summary

        aws_sdk_cloudformation.types.stack_resource_drift_information_summary.serialize_query(
            value["drift_information"], pairs, f"{prefix}.DriftInformation"
        )
    if "module_info" in value:
        import aws_sdk_cloudformation.types.module_info

        aws_sdk_cloudformation.types.module_info.serialize_query(
            value["module_info"], pairs, f"{prefix}.ModuleInfo"
        )


def deserialize_query(el: Element) -> StackResourceSummary:
    out: StackResourceSummary = {}  # type: ignore[typeddict-item]
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_physical_resource_id = el.find("PhysicalResourceId")
    if child_physical_resource_id is not None:
        out["physical_resource_id"] = str(child_physical_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_last_updated_timestamp = el.find("LastUpdatedTimestamp")
    if child_last_updated_timestamp is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_cloudformation.types.timestamp.deserialize_query(
                child_last_updated_timestamp
            )
        )
    child_resource_status = el.find("ResourceStatus")
    if child_resource_status is not None:
        import aws_sdk_cloudformation.types.resource_status

        out["resource_status"] = (
            aws_sdk_cloudformation.types.resource_status.deserialize_query(
                child_resource_status
            )
        )
    child_resource_status_reason = el.find("ResourceStatusReason")
    if child_resource_status_reason is not None:
        out["resource_status_reason"] = str(child_resource_status_reason.text or "")
    child_drift_information = el.find("DriftInformation")
    if child_drift_information is not None:
        import aws_sdk_cloudformation.types.stack_resource_drift_information_summary

        out["drift_information"] = (
            aws_sdk_cloudformation.types.stack_resource_drift_information_summary.deserialize_query(
                child_drift_information
            )
        )
    child_module_info = el.find("ModuleInfo")
    if child_module_info is not None:
        import aws_sdk_cloudformation.types.module_info

        out["module_info"] = aws_sdk_cloudformation.types.module_info.deserialize_query(
            child_module_info
        )
    return out
