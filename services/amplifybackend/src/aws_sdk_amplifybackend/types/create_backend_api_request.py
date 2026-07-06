"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendAPIRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.backend_api_resource_config


class CreateBackendAPIRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The name of the backend environment.</p>"""
    resource_config: NotRequired[
        "aws_sdk_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
    ]
    """<p>The resource configuration for this request.</p>"""
    resource_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendAPIRequest) -> dict:
    out: dict = {}
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "resource_config" in value:
        import aws_sdk_amplifybackend.types.backend_api_resource_config

        out["resourceConfig"] = (
            aws_sdk_amplifybackend.types.backend_api_resource_config.serialize_json(
                value["resource_config"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> CreateBackendAPIRequest:
    out: CreateBackendAPIRequest = {}  # type: ignore[typeddict-item]
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if "resourceConfig" in data:
        import aws_sdk_amplifybackend.types.backend_api_resource_config

        out["resource_config"] = (
            aws_sdk_amplifybackend.types.backend_api_resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out
