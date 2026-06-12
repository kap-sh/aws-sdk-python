"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceDrift``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.logical_resource_id
    import aws_sdk_cloudformation.types.module_info
    import aws_sdk_cloudformation.types.physical_resource_id
    import aws_sdk_cloudformation.types.physical_resource_id_context
    import aws_sdk_cloudformation.types.properties
    import aws_sdk_cloudformation.types.property_differences
    import aws_sdk_cloudformation.types.resource_type
    import aws_sdk_cloudformation.types.stack_id
    import aws_sdk_cloudformation.types.stack_resource_drift_status
    import aws_sdk_cloudformation.types.stack_resource_drift_status_reason
    import aws_sdk_cloudformation.types.timestamp


class StackResourceDrift(TypedDict):
    stack_id: NotRequired["aws_sdk_cloudformation.types.stack_id.StackId"]
    """<p>The ID of the stack.</p>"""
    logical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource specified in the template.</p>"""
    physical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.</p>"""
    physical_resource_id_context: NotRequired[
        "aws_sdk_cloudformation.types.physical_resource_id_context.PhysicalResourceIdContext"
    ]
    """<p>Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resource's logical and physical IDs aren't enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_cloudformation.types.resource_type.ResourceType"
    ]
    """<p>The type of the resource.</p>"""
    expected_properties: NotRequired[
        "aws_sdk_cloudformation.types.properties.Properties"
    ]
    """<p>A JSON structure that contains the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>"""
    actual_properties: NotRequired["aws_sdk_cloudformation.types.properties.Properties"]
    """<p>A JSON structure that contains the actual property values of the stack resource.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>"""
    property_differences: NotRequired[
        "aws_sdk_cloudformation.types.property_differences.PropertyDifferences"
    ]
    """<p>A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose <code>StackResourceDriftStatus</code> is <code>MODIFIED</code>.</p>"""
    stack_resource_drift_status: NotRequired[
        "aws_sdk_cloudformation.types.stack_resource_drift_status.StackResourceDriftStatus"
    ]
    """<p>Status of the resource's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration because the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation does not currently return this value.</p> </li> <li> <p> <code>UNKNOWN</code>: CloudFormation could not run drift detection for the resource. See the <code>DriftStatusReason</code> for details.</p> </li> </ul>"""
    timestamp: NotRequired["aws_sdk_cloudformation.types.timestamp.Timestamp"]
    """<p>Time at which CloudFormation performed drift detection on the stack resource.</p>"""
    module_info: NotRequired["aws_sdk_cloudformation.types.module_info.ModuleInfo"]
    """<p>Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.</p>"""
    drift_status_reason: NotRequired[
        "aws_sdk_cloudformation.types.stack_resource_drift_status_reason.StackResourceDriftStatusReason"
    ]
    """<p>The reason for the drift status. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceDrift, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_id" in value:
        pairs.append((f"{prefix}.StackId", str(value["stack_id"])))
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))
    if "physical_resource_id" in value:
        pairs.append(
            (f"{prefix}.PhysicalResourceId", str(value["physical_resource_id"]))
        )
    if "physical_resource_id_context" in value:
        import aws_sdk_cloudformation.types.physical_resource_id_context

        aws_sdk_cloudformation.types.physical_resource_id_context.serialize_query(
            value["physical_resource_id_context"],
            pairs,
            f"{prefix}.PhysicalResourceIdContext",
        )
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "expected_properties" in value:
        pairs.append(
            (f"{prefix}.ExpectedProperties", str(value["expected_properties"]))
        )
    if "actual_properties" in value:
        pairs.append((f"{prefix}.ActualProperties", str(value["actual_properties"])))
    if "property_differences" in value:
        import aws_sdk_cloudformation.types.property_differences

        aws_sdk_cloudformation.types.property_differences.serialize_query(
            value["property_differences"], pairs, f"{prefix}.PropertyDifferences"
        )
    if "stack_resource_drift_status" in value:
        import aws_sdk_cloudformation.types.stack_resource_drift_status

        aws_sdk_cloudformation.types.stack_resource_drift_status.serialize_query(
            value["stack_resource_drift_status"],
            pairs,
            f"{prefix}.StackResourceDriftStatus",
        )
    if "timestamp" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )
    if "module_info" in value:
        import aws_sdk_cloudformation.types.module_info

        aws_sdk_cloudformation.types.module_info.serialize_query(
            value["module_info"], pairs, f"{prefix}.ModuleInfo"
        )
    if "drift_status_reason" in value:
        pairs.append((f"{prefix}.DriftStatusReason", str(value["drift_status_reason"])))


def deserialize_query(el: Element) -> StackResourceDrift:
    out: StackResourceDrift = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_physical_resource_id = el.find("PhysicalResourceId")
    if child_physical_resource_id is not None:
        out["physical_resource_id"] = str(child_physical_resource_id.text or "")
    child_physical_resource_id_context = el.find("PhysicalResourceIdContext")
    if child_physical_resource_id_context is not None:
        import aws_sdk_cloudformation.types.physical_resource_id_context

        out["physical_resource_id_context"] = (
            aws_sdk_cloudformation.types.physical_resource_id_context.deserialize_query(
                child_physical_resource_id_context
            )
        )
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_expected_properties = el.find("ExpectedProperties")
    if child_expected_properties is not None:
        out["expected_properties"] = str(child_expected_properties.text or "")
    child_actual_properties = el.find("ActualProperties")
    if child_actual_properties is not None:
        out["actual_properties"] = str(child_actual_properties.text or "")
    child_property_differences = el.find("PropertyDifferences")
    if child_property_differences is not None:
        import aws_sdk_cloudformation.types.property_differences

        out["property_differences"] = (
            aws_sdk_cloudformation.types.property_differences.deserialize_query(
                child_property_differences
            )
        )
    child_stack_resource_drift_status = el.find("StackResourceDriftStatus")
    if child_stack_resource_drift_status is not None:
        import aws_sdk_cloudformation.types.stack_resource_drift_status

        out["stack_resource_drift_status"] = (
            aws_sdk_cloudformation.types.stack_resource_drift_status.deserialize_query(
                child_stack_resource_drift_status
            )
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["timestamp"] = aws_sdk_cloudformation.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_module_info = el.find("ModuleInfo")
    if child_module_info is not None:
        import aws_sdk_cloudformation.types.module_info

        out["module_info"] = aws_sdk_cloudformation.types.module_info.deserialize_query(
            child_module_info
        )
    child_drift_status_reason = el.find("DriftStatusReason")
    if child_drift_status_reason is not None:
        out["drift_status_reason"] = str(child_drift_status_reason.text or "")
    return out
