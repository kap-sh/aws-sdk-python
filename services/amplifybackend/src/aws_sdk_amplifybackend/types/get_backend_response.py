"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetBackendResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.list_of__string


class GetBackendResponse(TypedDict, closed=True):
    amplify_feature_flags: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>A stringified version of the cli.json file for your Amplify project.</p>"""
    amplify_meta_config: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>A stringified version of the current configs for your Amplify project.</p>"""
    app_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    app_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of the app.</p>"""
    backend_environment_list: NotRequired[
        "aws_sdk_amplifybackend.types.list_of__string.ListOf__string"
    ]
    """<p>A list of backend environments in an array.</p>"""
    backend_environment_name: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The name of the backend environment.</p>"""
    error: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>If the request failed, this is the returned error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendResponse) -> dict:
    out: dict = {}
    if "amplify_feature_flags" in value:
        out["amplifyFeatureFlags"] = value["amplify_feature_flags"]
    if "amplify_meta_config" in value:
        out["amplifyMetaConfig"] = value["amplify_meta_config"]
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "app_name" in value:
        out["appName"] = value["app_name"]
    if "backend_environment_list" in value:
        import aws_sdk_amplifybackend.types.list_of__string

        out["backendEnvironmentList"] = (
            aws_sdk_amplifybackend.types.list_of__string.serialize_json(
                value["backend_environment_list"]
            )
        )
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> GetBackendResponse:
    out: GetBackendResponse = {}  # type: ignore[typeddict-item]
    if "amplifyFeatureFlags" in data:
        out["amplify_feature_flags"] = data["amplifyFeatureFlags"]
    if "amplifyMetaConfig" in data:
        out["amplify_meta_config"] = data["amplifyMetaConfig"]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "appName" in data:
        out["app_name"] = data["appName"]
    if "backendEnvironmentList" in data:
        import aws_sdk_amplifybackend.types.list_of__string

        out["backend_environment_list"] = (
            aws_sdk_amplifybackend.types.list_of__string.deserialize_json(
                data["backendEnvironmentList"]
            )
        )
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if "error" in data:
        out["error"] = data["error"]
    return out
