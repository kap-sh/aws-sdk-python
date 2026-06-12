"""Generated from Smithy shape ``com.amazonaws.appstream#ScriptDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.s3_location
    import aws_sdk_appstream.types.string


class ScriptDetails(TypedDict):
    script_s3_location: NotRequired["aws_sdk_appstream.types.s3_location.S3Location"]
    """<p>The S3 object location for the script.</p>"""
    executable_path: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The run path for the script.</p>"""
    executable_parameters: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The runtime parameters passed to the run path for the script.</p>"""
    timeout_in_seconds: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The run timeout, in seconds, for the script.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptDetails) -> dict:
    out: dict = {}
    if "script_s3_location" in value:
        import aws_sdk_appstream.types.s3_location

        out["ScriptS3Location"] = (
            aws_sdk_appstream.types.s3_location.serialize_aws_json_1_1(
                value["script_s3_location"]
            )
        )
    if "executable_path" in value:
        out["ExecutablePath"] = value["executable_path"]
    if "executable_parameters" in value:
        out["ExecutableParameters"] = value["executable_parameters"]
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScriptDetails:
    out: ScriptDetails = {}  # type: ignore[typeddict-item]
    if "ScriptS3Location" in data:
        import aws_sdk_appstream.types.s3_location

        out["script_s3_location"] = (
            aws_sdk_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["ScriptS3Location"]
            )
        )
    if "ExecutablePath" in data:
        out["executable_path"] = data["ExecutablePath"]
    if "ExecutableParameters" in data:
        out["executable_parameters"] = data["ExecutableParameters"]
    if "TimeoutInSeconds" in data:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    return out
