"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StepAutomationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.platform_command
    import aws_sdk_migrationhuborchestrator.types.platform_script_key
    import aws_sdk_migrationhuborchestrator.types.run_environment
    import aws_sdk_migrationhuborchestrator.types.target_type


class StepAutomationConfiguration(TypedDict, closed=True):
    script_location_s3_bucket: NotRequired["str"]
    """<p>The Amazon S3 bucket where the script is located.</p>"""
    script_location_s3_key: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.platform_script_key.PlatformScriptKey"
    ]
    """<p>The Amazon S3 key for the script location.</p>"""
    command: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.platform_command.PlatformCommand"
    ]
    """<p>The command to run the script.</p>"""
    run_environment: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.run_environment.RunEnvironment"
    ]
    """<p>The source or target environment.</p>"""
    target_type: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.target_type.TargetType"
    ]
    """<p>The servers on which to run the script.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepAutomationConfiguration) -> dict:
    out: dict = {}
    if "script_location_s3_bucket" in value:
        out["scriptLocationS3Bucket"] = value["script_location_s3_bucket"]
    if "script_location_s3_key" in value:
        import aws_sdk_migrationhuborchestrator.types.platform_script_key

        out["scriptLocationS3Key"] = (
            aws_sdk_migrationhuborchestrator.types.platform_script_key.serialize_json(
                value["script_location_s3_key"]
            )
        )
    if "command" in value:
        import aws_sdk_migrationhuborchestrator.types.platform_command

        out["command"] = (
            aws_sdk_migrationhuborchestrator.types.platform_command.serialize_json(
                value["command"]
            )
        )
    if "run_environment" in value:
        out["runEnvironment"] = value["run_environment"]
    if "target_type" in value:
        out["targetType"] = value["target_type"]
    return out


def deserialize_json(data: dict) -> StepAutomationConfiguration:
    out: StepAutomationConfiguration = {}  # type: ignore[typeddict-item]
    if "scriptLocationS3Bucket" in data:
        out["script_location_s3_bucket"] = data["scriptLocationS3Bucket"]
    if "scriptLocationS3Key" in data:
        import aws_sdk_migrationhuborchestrator.types.platform_script_key

        out["script_location_s3_key"] = (
            aws_sdk_migrationhuborchestrator.types.platform_script_key.deserialize_json(
                data["scriptLocationS3Key"]
            )
        )
    if "command" in data:
        import aws_sdk_migrationhuborchestrator.types.platform_command

        out["command"] = (
            aws_sdk_migrationhuborchestrator.types.platform_command.deserialize_json(
                data["command"]
            )
        )
    if "runEnvironment" in data:
        out["run_environment"] = data["runEnvironment"]
    if "targetType" in data:
        out["target_type"] = data["targetType"]
    return out
