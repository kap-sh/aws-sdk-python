"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeApplicationInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_arn
    import aws_sdk_panorama.types.application_instance_health_status
    import aws_sdk_panorama.types.application_instance_id
    import aws_sdk_panorama.types.application_instance_name
    import aws_sdk_panorama.types.application_instance_status
    import aws_sdk_panorama.types.application_instance_status_description
    import aws_sdk_panorama.types.default_runtime_context_device
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.device_name
    import aws_sdk_panorama.types.reported_runtime_context_states
    import aws_sdk_panorama.types.runtime_role_arn
    import aws_sdk_panorama.types.tag_map
    import aws_sdk_panorama.types.time_stamp


class DescribeApplicationInstanceResponse(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_panorama.types.application_instance_name.ApplicationInstanceName"
    ]
    """<p>The application instance's name.</p>"""
    description: NotRequired["aws_sdk_panorama.types.description.Description"]
    """<p>The application instance's description.</p>"""
    default_runtime_context_device: NotRequired[
        "aws_sdk_panorama.types.default_runtime_context_device.DefaultRuntimeContextDevice"
    ]
    """<p>The device's ID.</p>"""
    default_runtime_context_device_name: NotRequired[
        "aws_sdk_panorama.types.device_name.DeviceName"
    ]
    """<p>The device's bane.</p>"""
    application_instance_id_to_replace: NotRequired[
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    ]
    """<p>The ID of the application instance that this instance replaced.</p>"""
    runtime_role_arn: NotRequired[
        "aws_sdk_panorama.types.runtime_role_arn.RuntimeRoleArn"
    ]
    """<p>The application instance's runtime role ARN.</p>"""
    status: NotRequired[
        "aws_sdk_panorama.types.application_instance_status.ApplicationInstanceStatus"
    ]
    """<p>The application instance's status.</p>"""
    health_status: NotRequired[
        "aws_sdk_panorama.types.application_instance_health_status.ApplicationInstanceHealthStatus"
    ]
    """<p>The application instance's health status.</p>"""
    status_description: NotRequired[
        "aws_sdk_panorama.types.application_instance_status_description.ApplicationInstanceStatusDescription"
    ]
    """<p>The application instance's status description.</p>"""
    created_time: NotRequired["aws_sdk_panorama.types.time_stamp.TimeStamp"]
    """<p>When the application instance was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_panorama.types.time_stamp.TimeStamp"]
    """<p>The application instance was updated.</p>"""
    application_instance_id: NotRequired[
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    ]
    """<p>The application instance's ID.</p>"""
    arn: NotRequired[
        "aws_sdk_panorama.types.application_instance_arn.ApplicationInstanceArn"
    ]
    """<p>The application instance's ARN.</p>"""
    tags: NotRequired["aws_sdk_panorama.types.tag_map.TagMap"]
    """<p>The application instance's tags.</p>"""
    runtime_context_states: NotRequired[
        "aws_sdk_panorama.types.reported_runtime_context_states.ReportedRuntimeContextStates"
    ]
    """<p>The application instance's state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApplicationInstanceResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_runtime_context_device" in value:
        out["DefaultRuntimeContextDevice"] = value["default_runtime_context_device"]
    if "default_runtime_context_device_name" in value:
        out["DefaultRuntimeContextDeviceName"] = value[
            "default_runtime_context_device_name"
        ]
    if "application_instance_id_to_replace" in value:
        out["ApplicationInstanceIdToReplace"] = value[
            "application_instance_id_to_replace"
        ]
    if "runtime_role_arn" in value:
        out["RuntimeRoleArn"] = value["runtime_role_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "health_status" in value:
        out["HealthStatus"] = value["health_status"]
    if "status_description" in value:
        out["StatusDescription"] = value["status_description"]
    if "created_time" in value:
        import aws_sdk_panorama.types.time_stamp

        out["CreatedTime"] = aws_sdk_panorama.types.time_stamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_panorama.types.time_stamp

        out["LastUpdatedTime"] = aws_sdk_panorama.types.time_stamp.serialize_json(
            value["last_updated_time"]
        )
    if "application_instance_id" in value:
        out["ApplicationInstanceId"] = value["application_instance_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_panorama.types.tag_map

        out["Tags"] = aws_sdk_panorama.types.tag_map.serialize_json(value["tags"])
    if "runtime_context_states" in value:
        import aws_sdk_panorama.types.reported_runtime_context_states

        out["RuntimeContextStates"] = (
            aws_sdk_panorama.types.reported_runtime_context_states.serialize_json(
                value["runtime_context_states"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeApplicationInstanceResponse:
    out: DescribeApplicationInstanceResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultRuntimeContextDevice" in data:
        out["default_runtime_context_device"] = data["DefaultRuntimeContextDevice"]
    if "DefaultRuntimeContextDeviceName" in data:
        out["default_runtime_context_device_name"] = data[
            "DefaultRuntimeContextDeviceName"
        ]
    if "ApplicationInstanceIdToReplace" in data:
        out["application_instance_id_to_replace"] = data[
            "ApplicationInstanceIdToReplace"
        ]
    if "RuntimeRoleArn" in data:
        out["runtime_role_arn"] = data["RuntimeRoleArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "HealthStatus" in data:
        out["health_status"] = data["HealthStatus"]
    if "StatusDescription" in data:
        out["status_description"] = data["StatusDescription"]
    if "CreatedTime" in data:
        import aws_sdk_panorama.types.time_stamp

        out["created_time"] = aws_sdk_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_panorama.types.time_stamp

        out["last_updated_time"] = aws_sdk_panorama.types.time_stamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "ApplicationInstanceId" in data:
        out["application_instance_id"] = data["ApplicationInstanceId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Tags" in data:
        import aws_sdk_panorama.types.tag_map

        out["tags"] = aws_sdk_panorama.types.tag_map.deserialize_json(data["Tags"])
    if "RuntimeContextStates" in data:
        import aws_sdk_panorama.types.reported_runtime_context_states

        out["runtime_context_states"] = (
            aws_sdk_panorama.types.reported_runtime_context_states.deserialize_json(
                data["RuntimeContextStates"]
            )
        )
    return out
