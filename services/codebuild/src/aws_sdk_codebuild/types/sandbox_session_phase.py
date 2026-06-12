"""Generated from Smithy shape ``com.amazonaws.codebuild#SandboxSessionPhase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.phase_contexts
    import aws_sdk_codebuild.types.status_type
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.timestamp
    import aws_sdk_codebuild.types.wrapper_long


class SandboxSessionPhase(TypedDict):
    phase_type: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The name of the sandbox phase.</p>"""
    phase_status: NotRequired["aws_sdk_codebuild.types.status_type.StatusType"]
    """<p>The current status of the sandbox phase. Valid values include:</p> <dl> <dt>FAILED</dt> <dd> <p>The sandbox phase failed.</p> </dd> <dt>FAULT</dt> <dd> <p>The sandbox phase faulted.</p> </dd> <dt>IN_PROGRESS</dt> <dd> <p>The sandbox phase is still in progress.</p> </dd> <dt>STOPPED</dt> <dd> <p>The sandbox phase stopped.</p> </dd> <dt>SUCCEEDED</dt> <dd> <p>The sandbox phase succeeded.</p> </dd> <dt>TIMED_OUT</dt> <dd> <p>The sandbox phase timed out.</p> </dd> </dl>"""
    start_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox phase started, expressed in Unix time format.</p>"""
    end_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox phase ended, expressed in Unix time format.</p>"""
    duration_in_seconds: NotRequired["aws_sdk_codebuild.types.wrapper_long.WrapperLong"]
    """<p>How long, in seconds, between the starting and ending times of the sandbox's phase.</p>"""
    contexts: NotRequired["aws_sdk_codebuild.types.phase_contexts.PhaseContexts"]
    """<p> An array of <code>PhaseContext</code> objects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SandboxSessionPhase) -> dict:
    out: dict = {}
    if "phase_type" in value:
        out["phaseType"] = value["phase_type"]
    if "phase_status" in value:
        import aws_sdk_codebuild.types.status_type

        out["phaseStatus"] = aws_sdk_codebuild.types.status_type.serialize_aws_json_1_1(
            value["phase_status"]
        )
    if "start_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["startTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["endTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "duration_in_seconds" in value:
        out["durationInSeconds"] = value["duration_in_seconds"]
    if "contexts" in value:
        import aws_sdk_codebuild.types.phase_contexts

        out["contexts"] = aws_sdk_codebuild.types.phase_contexts.serialize_aws_json_1_1(
            value["contexts"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SandboxSessionPhase:
    out: SandboxSessionPhase = {}  # type: ignore[typeddict-item]
    if "phaseType" in data:
        out["phase_type"] = data["phaseType"]
    if "phaseStatus" in data:
        import aws_sdk_codebuild.types.status_type

        out["phase_status"] = (
            aws_sdk_codebuild.types.status_type.deserialize_aws_json_1_1(
                data["phaseStatus"]
            )
        )
    if "startTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["start_time"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["end_time"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "durationInSeconds" in data:
        out["duration_in_seconds"] = data["durationInSeconds"]
    if "contexts" in data:
        import aws_sdk_codebuild.types.phase_contexts

        out["contexts"] = (
            aws_sdk_codebuild.types.phase_contexts.deserialize_aws_json_1_1(
                data["contexts"]
            )
        )
    return out
