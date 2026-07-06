"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendAuthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.create_backend_auth_resource_config


class CreateBackendAuthRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The name of the backend environment.</p>"""
    resource_config: NotRequired[
        "aws_sdk_amplifybackend.types.create_backend_auth_resource_config.CreateBackendAuthResourceConfig"
    ]
    """<p>The resource configuration for this request object.</p>"""
    resource_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendAuthRequest) -> dict:
    out: dict = {}
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "resource_config" in value:
        import aws_sdk_amplifybackend.types.create_backend_auth_resource_config

        out["resourceConfig"] = (
            aws_sdk_amplifybackend.types.create_backend_auth_resource_config.serialize_json(
                value["resource_config"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> CreateBackendAuthRequest:
    out: CreateBackendAuthRequest = {}  # type: ignore[typeddict-item]
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if "resourceConfig" in data:
        import aws_sdk_amplifybackend.types.create_backend_auth_resource_config

        out["resource_config"] = (
            aws_sdk_amplifybackend.types.create_backend_auth_resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out
