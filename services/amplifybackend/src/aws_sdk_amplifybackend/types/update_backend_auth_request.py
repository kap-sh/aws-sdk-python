"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.update_backend_auth_resource_config


class UpdateBackendAuthRequest(TypedDict):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    resource_config: NotRequired[
        "aws_sdk_amplifybackend.types.update_backend_auth_resource_config.UpdateBackendAuthResourceConfig"
    ]
    """<p>The resource configuration for this request object.</p>"""
    resource_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthRequest) -> dict:
    out: dict = {}
    if "resource_config" in value:
        import aws_sdk_amplifybackend.types.update_backend_auth_resource_config

        out["resourceConfig"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_resource_config.serialize_json(
                value["resource_config"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthRequest:
    out: UpdateBackendAuthRequest = {}  # type: ignore[typeddict-item]
    if "resourceConfig" in data:
        import aws_sdk_amplifybackend.types.update_backend_auth_resource_config

        out["resource_config"] = (
            aws_sdk_amplifybackend.types.update_backend_auth_resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out
