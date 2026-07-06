"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeApplicationInstanceDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_id
    import aws_sdk_panorama.types.application_instance_name
    import aws_sdk_panorama.types.default_runtime_context_device
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.manifest_overrides_payload
    import aws_sdk_panorama.types.manifest_payload
    import aws_sdk_panorama.types.time_stamp


class DescribeApplicationInstanceDetailsResponse(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_panorama.types.application_instance_name.ApplicationInstanceName"
    ]
    """<p>The application instance's name.</p>"""
    description: NotRequired["aws_sdk_panorama.types.description.Description"]
    """<p>The application instance's description.</p>"""
    default_runtime_context_device: NotRequired[
        "aws_sdk_panorama.types.default_runtime_context_device.DefaultRuntimeContextDevice"
    ]
    """<p>The application instance's default runtime context device.</p>"""
    manifest_payload: NotRequired[
        "aws_sdk_panorama.types.manifest_payload.ManifestPayload"
    ]
    """<p>The application instance's configuration manifest.</p>"""
    manifest_overrides_payload: NotRequired[
        "aws_sdk_panorama.types.manifest_overrides_payload.ManifestOverridesPayload"
    ]
    """<p>Parameter overrides for the configuration manifest.</p>"""
    application_instance_id_to_replace: NotRequired[
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    ]
    """<p>The ID of the application instance that this instance replaced.</p>"""
    created_time: NotRequired["aws_sdk_panorama.types.time_stamp.TimeStamp"]
    """<p>When the application instance was created.</p>"""
    application_instance_id: NotRequired[
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    ]
    """<p>The application instance's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApplicationInstanceDetailsResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_runtime_context_device" in value:
        out["DefaultRuntimeContextDevice"] = value["default_runtime_context_device"]
    if "manifest_payload" in value:
        import aws_sdk_panorama.types.manifest_payload

        out["ManifestPayload"] = aws_sdk_panorama.types.manifest_payload.serialize_json(
            value["manifest_payload"]
        )
    if "manifest_overrides_payload" in value:
        import aws_sdk_panorama.types.manifest_overrides_payload

        out["ManifestOverridesPayload"] = (
            aws_sdk_panorama.types.manifest_overrides_payload.serialize_json(
                value["manifest_overrides_payload"]
            )
        )
    if "application_instance_id_to_replace" in value:
        out["ApplicationInstanceIdToReplace"] = value[
            "application_instance_id_to_replace"
        ]
    if "created_time" in value:
        import aws_sdk_panorama.types.time_stamp

        out["CreatedTime"] = aws_sdk_panorama.types.time_stamp.serialize_json(
            value["created_time"]
        )
    if "application_instance_id" in value:
        out["ApplicationInstanceId"] = value["application_instance_id"]
    return out


def deserialize_json(data: dict) -> DescribeApplicationInstanceDetailsResponse:
    out: DescribeApplicationInstanceDetailsResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultRuntimeContextDevice" in data:
        out["default_runtime_context_device"] = data["DefaultRuntimeContextDevice"]
    if "ManifestPayload" in data:
        import aws_sdk_panorama.types.manifest_payload

        out["manifest_payload"] = (
            aws_sdk_panorama.types.manifest_payload.deserialize_json(
                data["ManifestPayload"]
            )
        )
    if "ManifestOverridesPayload" in data:
        import aws_sdk_panorama.types.manifest_overrides_payload

        out["manifest_overrides_payload"] = (
            aws_sdk_panorama.types.manifest_overrides_payload.deserialize_json(
                data["ManifestOverridesPayload"]
            )
        )
    if "ApplicationInstanceIdToReplace" in data:
        out["application_instance_id_to_replace"] = data[
            "ApplicationInstanceIdToReplace"
        ]
    if "CreatedTime" in data:
        import aws_sdk_panorama.types.time_stamp

        out["created_time"] = aws_sdk_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    if "ApplicationInstanceId" in data:
        out["application_instance_id"] = data["ApplicationInstanceId"]
    return out
