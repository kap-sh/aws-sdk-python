"""Generated from Smithy shape ``com.amazonaws.panorama#ApplicationInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.application_instance_arn
    import capo_panorama.types.application_instance_health_status
    import capo_panorama.types.application_instance_id
    import capo_panorama.types.application_instance_name
    import capo_panorama.types.application_instance_status
    import capo_panorama.types.application_instance_status_description
    import capo_panorama.types.default_runtime_context_device
    import capo_panorama.types.description
    import capo_panorama.types.device_name
    import capo_panorama.types.reported_runtime_context_states
    import capo_panorama.types.tag_map
    import capo_panorama.types.time_stamp


class ApplicationInstance(TypedDict, closed=True):
    name: NotRequired[
        "capo_panorama.types.application_instance_name.ApplicationInstanceName"
    ]
    """<p>The application instance's name.</p>"""
    application_instance_id: NotRequired[
        "capo_panorama.types.application_instance_id.ApplicationInstanceId"
    ]
    """<p>The application instance's ID.</p>"""
    default_runtime_context_device: NotRequired[
        "capo_panorama.types.default_runtime_context_device.DefaultRuntimeContextDevice"
    ]
    """<p>The device's ID.</p>"""
    default_runtime_context_device_name: NotRequired[
        "capo_panorama.types.device_name.DeviceName"
    ]
    """<p>The device's name.</p>"""
    description: NotRequired["capo_panorama.types.description.Description"]
    """<p>The application instance's description.</p>"""
    status: NotRequired[
        "capo_panorama.types.application_instance_status.ApplicationInstanceStatus"
    ]
    """<p>The application instance's status.</p>"""
    health_status: NotRequired[
        "capo_panorama.types.application_instance_health_status.ApplicationInstanceHealthStatus"
    ]
    """<p>The application instance's health status.</p>"""
    status_description: NotRequired[
        "capo_panorama.types.application_instance_status_description.ApplicationInstanceStatusDescription"
    ]
    """<p>The application instance's status description.</p>"""
    created_time: NotRequired["capo_panorama.types.time_stamp.TimeStamp"]
    """<p>When the application instance was created.</p>"""
    arn: NotRequired[
        "capo_panorama.types.application_instance_arn.ApplicationInstanceArn"
    ]
    """<p>The application instance's ARN.</p>"""
    tags: NotRequired["capo_panorama.types.tag_map.TagMap"]
    """<p>The application instance's tags.</p>"""
    runtime_context_states: NotRequired[
        "capo_panorama.types.reported_runtime_context_states.ReportedRuntimeContextStates"
    ]
    """<p>The application's state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationInstance) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "application_instance_id" in value:
        out["ApplicationInstanceId"] = value["application_instance_id"]
    if "default_runtime_context_device" in value:
        out["DefaultRuntimeContextDevice"] = value["default_runtime_context_device"]
    if "default_runtime_context_device_name" in value:
        out["DefaultRuntimeContextDeviceName"] = value[
            "default_runtime_context_device_name"
        ]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        out["Status"] = value["status"]
    if "health_status" in value:
        out["HealthStatus"] = value["health_status"]
    if "status_description" in value:
        out["StatusDescription"] = value["status_description"]
    if "created_time" in value:
        import capo_panorama.types.time_stamp

        out["CreatedTime"] = capo_panorama.types.time_stamp.serialize_json(
            value["created_time"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import capo_panorama.types.tag_map

        out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    if "runtime_context_states" in value:
        import capo_panorama.types.reported_runtime_context_states

        out["RuntimeContextStates"] = (
            capo_panorama.types.reported_runtime_context_states.serialize_json(
                value["runtime_context_states"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationInstance:
    out: ApplicationInstance = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ApplicationInstanceId" in data:
        out["application_instance_id"] = data["ApplicationInstanceId"]
    if "DefaultRuntimeContextDevice" in data:
        out["default_runtime_context_device"] = data["DefaultRuntimeContextDevice"]
    if "DefaultRuntimeContextDeviceName" in data:
        out["default_runtime_context_device_name"] = data[
            "DefaultRuntimeContextDeviceName"
        ]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "HealthStatus" in data:
        out["health_status"] = data["HealthStatus"]
    if "StatusDescription" in data:
        out["status_description"] = data["StatusDescription"]
    if "CreatedTime" in data:
        import capo_panorama.types.time_stamp

        out["created_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Tags" in data:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    if "RuntimeContextStates" in data:
        import capo_panorama.types.reported_runtime_context_states

        out["runtime_context_states"] = (
            capo_panorama.types.reported_runtime_context_states.deserialize_json(
                data["RuntimeContextStates"]
            )
        )
    return out
