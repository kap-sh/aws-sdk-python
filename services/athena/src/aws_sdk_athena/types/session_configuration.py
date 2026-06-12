"""Generated from Smithy shape ``com.amazonaws.athena#SessionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.encryption_configuration
    import aws_sdk_athena.types.long
    import aws_sdk_athena.types.result_output_location
    import aws_sdk_athena.types.role_arn
    import aws_sdk_athena.types.session_idle_timeout_in_minutes


class SessionConfiguration(TypedDict):
    execution_role: NotRequired["aws_sdk_athena.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.</p>"""
    working_directory: NotRequired[
        "aws_sdk_athena.types.result_output_location.ResultOutputLocation"
    ]
    """<p>The Amazon S3 location that stores information for the notebook.</p>"""
    idle_timeout_seconds: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The idle timeout in seconds for the session.</p>"""
    session_idle_timeout_in_minutes: NotRequired[
        "aws_sdk_athena.types.session_idle_timeout_in_minutes.SessionIdleTimeoutInMinutes"
    ]
    """<p>The idle timeout in seconds for the session.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_athena.types.encryption_configuration.EncryptionConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionConfiguration) -> dict:
    out: dict = {}
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "idle_timeout_seconds" in value:
        out["IdleTimeoutSeconds"] = value["idle_timeout_seconds"]
    if "session_idle_timeout_in_minutes" in value:
        out["SessionIdleTimeoutInMinutes"] = value["session_idle_timeout_in_minutes"]
    if "encryption_configuration" in value:
        import aws_sdk_athena.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_athena.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionConfiguration:
    out: SessionConfiguration = {}  # type: ignore[typeddict-item]
    if "ExecutionRole" in data:
        out["execution_role"] = data["ExecutionRole"]
    if "WorkingDirectory" in data:
        out["working_directory"] = data["WorkingDirectory"]
    if "IdleTimeoutSeconds" in data:
        out["idle_timeout_seconds"] = data["IdleTimeoutSeconds"]
    if "SessionIdleTimeoutInMinutes" in data:
        out["session_idle_timeout_in_minutes"] = data["SessionIdleTimeoutInMinutes"]
    if "EncryptionConfiguration" in data:
        import aws_sdk_athena.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_athena.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out
