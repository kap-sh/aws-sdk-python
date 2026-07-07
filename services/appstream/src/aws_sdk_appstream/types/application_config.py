"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_display_name
    import aws_sdk_appstream.types.app_name
    import aws_sdk_appstream.types.file_path
    import aws_sdk_appstream.types.launch_parameters


class ApplicationConfig(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appstream.types.app_name.AppName"]
    """<p>The name of the application. This is a required field that must be unique within the application catalog and between 1-100 characters, matching the pattern ^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,99}$.</p>"""
    display_name: NotRequired["aws_sdk_appstream.types.app_display_name.AppDisplayName"]
    """<p>The display name shown to users for this application. This field is optional and can be 0-100 characters, matching the pattern ^[a-zA-Z0-9][a-zA-Z0-9_. -]{0,99}$.</p>"""
    absolute_app_path: NotRequired["aws_sdk_appstream.types.file_path.FilePath"]
    r"""<p>The absolute path to the executable file that launches the application. This is a required field that can be 1-32767 characters to support Windows extended file paths. Use escaped file path strings like \"C:\\\\Windows\\\\System32\\\\notepad.exe\".</p>"""
    absolute_icon_path: NotRequired["aws_sdk_appstream.types.file_path.FilePath"]
    """<p>The absolute path to the icon file for the application. This field is optional and can be 1-32767 characters. If not provided, the icon is derived from the executable. Use PNG images with proper transparency for the best user experience.</p>"""
    absolute_manifest_path: NotRequired["aws_sdk_appstream.types.file_path.FilePath"]
    """<p>The absolute path to the prewarm manifest file for this application. This field is optional and only applicable when using application-specific manifests. The path can be 1-32767 characters and should point to a text file containing file paths to prewarm.</p>"""
    working_directory: NotRequired["aws_sdk_appstream.types.file_path.FilePath"]
    r"""<p>The working directory to use when launching the application. This field is optional and can be 0-32767 characters. Use escaped file path strings like \"C:\\\\Path\\\\To\\\\Working\\\\Directory\".</p>"""
    launch_parameters: NotRequired[
        "aws_sdk_appstream.types.launch_parameters.LaunchParameters"
    ]
    """<p>The launch parameters to pass to the application executable. This field is optional and can be 0-1024 characters. Use escaped strings with the full list of required parameters, such as PowerShell script paths or command-line arguments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "absolute_app_path" in value:
        out["AbsoluteAppPath"] = value["absolute_app_path"]
    if "absolute_icon_path" in value:
        out["AbsoluteIconPath"] = value["absolute_icon_path"]
    if "absolute_manifest_path" in value:
        out["AbsoluteManifestPath"] = value["absolute_manifest_path"]
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "launch_parameters" in value:
        out["LaunchParameters"] = value["launch_parameters"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationConfig:
    out: ApplicationConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "AbsoluteAppPath" in data:
        out["absolute_app_path"] = data["AbsoluteAppPath"]
    if "AbsoluteIconPath" in data:
        out["absolute_icon_path"] = data["AbsoluteIconPath"]
    if "AbsoluteManifestPath" in data:
        out["absolute_manifest_path"] = data["AbsoluteManifestPath"]
    if "WorkingDirectory" in data:
        out["working_directory"] = data["WorkingDirectory"]
    if "LaunchParameters" in data:
        out["launch_parameters"] = data["LaunchParameters"]
    return out
