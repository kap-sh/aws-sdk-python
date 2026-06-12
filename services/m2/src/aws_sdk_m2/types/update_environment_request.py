"""Generated from Smithy shape ``com.amazonaws.m2#UpdateEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_m2.types.boolean
    import aws_sdk_m2.types.capacity_value
    import aws_sdk_m2.types.engine_version
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.string20


class UpdateEnvironmentRequest(TypedDict):
    environment_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment that you want to update.</p>"""
    desired_capacity: NotRequired["aws_sdk_m2.types.capacity_value.CapacityValue"]
    """<p>The desired capacity for the runtime environment to update. The minimum possible value is 0 and the maximum is 100.</p>"""
    instance_type: NotRequired["aws_sdk_m2.types.string20.String20"]
    """<p>The instance type for the runtime environment to update.</p>"""
    engine_version: NotRequired["aws_sdk_m2.types.engine_version.EngineVersion"]
    """<p>The version of the runtime engine for the runtime environment.</p>"""
    preferred_maintenance_window: NotRequired["str"]
    """<p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>"""
    apply_during_maintenance_window: "aws_sdk_m2.types.boolean.Boolean"
    """<p>Indicates whether to update the runtime environment during the maintenance window. The default is false. Currently, Amazon Web Services Mainframe Modernization accepts the <code>engineVersion</code> parameter only if <code>applyDuringMaintenanceWindow</code> is true. If any parameter other than <code>engineVersion</code> is provided in <code>UpdateEnvironmentRequest</code>, it will fail if <code>applyDuringMaintenanceWindow</code> is set to true.</p>"""
    force_update: "aws_sdk_m2.types.boolean.Boolean"
    """<p>Forces the updates on the environment. This option is needed if the applications in the environment are not stopped or if there are ongoing application-related activities in the environment.</p> <p>If you use this option, be aware that it could lead to data corruption in the applications, and that you might need to perform repair and recovery procedures for the applications.</p> <p>This option is not needed if the attribute being updated is <code>preferredMaintenanceWindow</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentRequest) -> dict:
    out: dict = {}
    if "desired_capacity" in value:
        out["desiredCapacity"] = value["desired_capacity"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    out["applyDuringMaintenanceWindow"] = value.get(
        "apply_during_maintenance_window", False
    )
    out["forceUpdate"] = value.get("force_update", False)
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentRequest:
    out: UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "desiredCapacity" in data:
        out["desired_capacity"] = data["desiredCapacity"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    if "preferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if "applyDuringMaintenanceWindow" in data:
        out["apply_during_maintenance_window"] = data["applyDuringMaintenanceWindow"]
    else:
        out["apply_during_maintenance_window"] = False
    if "forceUpdate" in data:
        out["force_update"] = data["forceUpdate"]
    else:
        out["force_update"] = False
    return out
