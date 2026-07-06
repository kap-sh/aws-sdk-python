"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.resource_config


class CreateBackendRequest(TypedDict, closed=True):
    app_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    app_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of the app.</p>"""
    backend_environment_name: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The name of the backend environment.</p>"""
    resource_config: NotRequired[
        "aws_sdk_amplifybackend.types.resource_config.ResourceConfig"
    ]
    """<p>The resource configuration for creating a backend.</p>"""
    resource_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendRequest) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "app_name" in value:
        out["appName"] = value["app_name"]
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "resource_config" in value:
        import aws_sdk_amplifybackend.types.resource_config

        out["resourceConfig"] = (
            aws_sdk_amplifybackend.types.resource_config.serialize_json(
                value["resource_config"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> CreateBackendRequest:
    out: CreateBackendRequest = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "appName" in data:
        out["app_name"] = data["appName"]
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if "resourceConfig" in data:
        import aws_sdk_amplifybackend.types.resource_config

        out["resource_config"] = (
            aws_sdk_amplifybackend.types.resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out
