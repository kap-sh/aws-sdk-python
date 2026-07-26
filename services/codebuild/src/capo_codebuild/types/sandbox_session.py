"""Generated from Smithy shape ``com.amazonaws.codebuild#SandboxSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.logs_location
    import capo_codebuild.types.network_interface
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.sandbox_session_phases
    import capo_codebuild.types.string
    import capo_codebuild.types.timestamp


class SandboxSession(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the sandbox session.</p>"""
    status: NotRequired["capo_codebuild.types.string.String"]
    """<p>The status of the sandbox session.</p>"""
    start_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox session started, expressed in Unix time format.</p>"""
    end_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox session ended, expressed in Unix time format.</p>"""
    current_phase: NotRequired["capo_codebuild.types.string.String"]
    """<p>The current phase for the sandbox.</p>"""
    phases: NotRequired[
        "capo_codebuild.types.sandbox_session_phases.SandboxSessionPhases"
    ]
    """<p> An array of <code>SandboxSessionPhase</code> objects. </p>"""
    resolved_source_version: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>An identifier for the version of this sandbox's source code.</p>"""
    logs: NotRequired["capo_codebuild.types.logs_location.LogsLocation"]
    network_interface: NotRequired[
        "capo_codebuild.types.network_interface.NetworkInterface"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SandboxSession) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "start_time" in value:
        import capo_codebuild.types.timestamp

        out["startTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codebuild.types.timestamp

        out["endTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "current_phase" in value:
        out["currentPhase"] = value["current_phase"]
    if "phases" in value:
        import capo_codebuild.types.sandbox_session_phases

        out["phases"] = (
            capo_codebuild.types.sandbox_session_phases.serialize_aws_json_1_1(
                value["phases"]
            )
        )
    if "resolved_source_version" in value:
        out["resolvedSourceVersion"] = value["resolved_source_version"]
    if "logs" in value:
        import capo_codebuild.types.logs_location

        out["logs"] = capo_codebuild.types.logs_location.serialize_aws_json_1_1(
            value["logs"]
        )
    if "network_interface" in value:
        import capo_codebuild.types.network_interface

        out["networkInterface"] = (
            capo_codebuild.types.network_interface.serialize_aws_json_1_1(
                value["network_interface"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SandboxSession:
    out: SandboxSession = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "startTime" in data:
        import capo_codebuild.types.timestamp

        out["start_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_codebuild.types.timestamp

        out["end_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "currentPhase" in data:
        out["current_phase"] = data["currentPhase"]
    if "phases" in data:
        import capo_codebuild.types.sandbox_session_phases

        out["phases"] = (
            capo_codebuild.types.sandbox_session_phases.deserialize_aws_json_1_1(
                data["phases"]
            )
        )
    if "resolvedSourceVersion" in data:
        out["resolved_source_version"] = data["resolvedSourceVersion"]
    if "logs" in data:
        import capo_codebuild.types.logs_location

        out["logs"] = capo_codebuild.types.logs_location.deserialize_aws_json_1_1(
            data["logs"]
        )
    if "networkInterface" in data:
        import capo_codebuild.types.network_interface

        out["network_interface"] = (
            capo_codebuild.types.network_interface.deserialize_aws_json_1_1(
                data["networkInterface"]
            )
        )
    return out
