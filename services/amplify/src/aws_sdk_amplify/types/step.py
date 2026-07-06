"""Generated from Smithy shape ``com.amazonaws.amplify#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.artifacts_url
    import aws_sdk_amplify.types.context
    import aws_sdk_amplify.types.end_time
    import aws_sdk_amplify.types.job_status
    import aws_sdk_amplify.types.log_url
    import aws_sdk_amplify.types.screenshots
    import aws_sdk_amplify.types.start_time
    import aws_sdk_amplify.types.status_reason
    import aws_sdk_amplify.types.step_name
    import aws_sdk_amplify.types.test_artifacts_url
    import aws_sdk_amplify.types.test_config_url


class Step(TypedDict, closed=True):
    step_name: "aws_sdk_amplify.types.step_name.StepName"
    """<p> The name of the execution step. </p>"""
    start_time: "aws_sdk_amplify.types.start_time.StartTime"
    """<p> The start date and time of the execution step. </p>"""
    status: "aws_sdk_amplify.types.job_status.JobStatus"
    """<p> The status of the execution step. </p>"""
    end_time: "aws_sdk_amplify.types.end_time.EndTime"
    """<p> The end date and time of the execution step. </p>"""
    log_url: NotRequired["aws_sdk_amplify.types.log_url.LogUrl"]
    """<p> The URL to the logs for the execution step. </p>"""
    artifacts_url: NotRequired["aws_sdk_amplify.types.artifacts_url.ArtifactsUrl"]
    """<p> The URL to the build artifact for the execution step. </p>"""
    test_artifacts_url: NotRequired[
        "aws_sdk_amplify.types.test_artifacts_url.TestArtifactsUrl"
    ]
    """<p> The URL to the test artifact for the execution step. </p>"""
    test_config_url: NotRequired["aws_sdk_amplify.types.test_config_url.TestConfigUrl"]
    """<p> The URL to the test configuration for the execution step. </p>"""
    screenshots: NotRequired["aws_sdk_amplify.types.screenshots.Screenshots"]
    """<p> The list of screenshot URLs for the execution step, if relevant. </p>"""
    status_reason: NotRequired["aws_sdk_amplify.types.status_reason.StatusReason"]
    """<p> The reason for the current step status. </p>"""
    context: NotRequired["aws_sdk_amplify.types.context.Context"]
    """<p> The context for the current step. Includes a build image if the step is build. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
    out: dict = {}
    out["stepName"] = value["step_name"]
    import aws_sdk_amplify.types.start_time

    out["startTime"] = aws_sdk_amplify.types.start_time.serialize_json(
        value["start_time"]
    )
    import aws_sdk_amplify.types.job_status

    out["status"] = aws_sdk_amplify.types.job_status.serialize_json(value["status"])
    import aws_sdk_amplify.types.end_time

    out["endTime"] = aws_sdk_amplify.types.end_time.serialize_json(value["end_time"])
    if "log_url" in value:
        out["logUrl"] = value["log_url"]
    if "artifacts_url" in value:
        out["artifactsUrl"] = value["artifacts_url"]
    if "test_artifacts_url" in value:
        out["testArtifactsUrl"] = value["test_artifacts_url"]
    if "test_config_url" in value:
        out["testConfigUrl"] = value["test_config_url"]
    if "screenshots" in value:
        import aws_sdk_amplify.types.screenshots

        out["screenshots"] = aws_sdk_amplify.types.screenshots.serialize_json(
            value["screenshots"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "context" in value:
        out["context"] = value["context"]
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if "stepName" in data:
        out["step_name"] = data["stepName"]
    else:
        raise DeserializationError("Step.step_name required")
    if "startTime" in data:
        import aws_sdk_amplify.types.start_time

        out["start_time"] = aws_sdk_amplify.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("Step.start_time required")
    if "status" in data:
        import aws_sdk_amplify.types.job_status

        out["status"] = aws_sdk_amplify.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("Step.status required")
    if "endTime" in data:
        import aws_sdk_amplify.types.end_time

        out["end_time"] = aws_sdk_amplify.types.end_time.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("Step.end_time required")
    if "logUrl" in data:
        out["log_url"] = data["logUrl"]
    if "artifactsUrl" in data:
        out["artifacts_url"] = data["artifactsUrl"]
    if "testArtifactsUrl" in data:
        out["test_artifacts_url"] = data["testArtifactsUrl"]
    if "testConfigUrl" in data:
        out["test_config_url"] = data["testConfigUrl"]
    if "screenshots" in data:
        import aws_sdk_amplify.types.screenshots

        out["screenshots"] = aws_sdk_amplify.types.screenshots.deserialize_json(
            data["screenshots"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "context" in data:
        out["context"] = data["context"]
    return out
