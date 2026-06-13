"""Generated from Smithy shape ``com.amazonaws.inspector2#StopCisSessionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.benchmark_profile
    import aws_sdk_inspector2.types.benchmark_version
    import aws_sdk_inspector2.types.compute_platform
    import aws_sdk_inspector2.types.reason
    import aws_sdk_inspector2.types.stop_cis_message_progress
    import aws_sdk_inspector2.types.stop_cis_session_status


class StopCisSessionMessage(TypedDict):
    status: "aws_sdk_inspector2.types.stop_cis_session_status.StopCisSessionStatus"
    """<p>The status of the message.</p>"""
    reason: NotRequired["aws_sdk_inspector2.types.reason.Reason"]
    """<p>The reason for the message.</p>"""
    progress: (
        "aws_sdk_inspector2.types.stop_cis_message_progress.StopCisMessageProgress"
    )
    """<p>The progress of the message.</p>"""
    compute_platform: NotRequired[
        "aws_sdk_inspector2.types.compute_platform.ComputePlatform"
    ]
    """<p>The message compute platform.</p>"""
    benchmark_version: NotRequired[
        "aws_sdk_inspector2.types.benchmark_version.BenchmarkVersion"
    ]
    """<p>The message benchmark version.</p>"""
    benchmark_profile: NotRequired[
        "aws_sdk_inspector2.types.benchmark_profile.BenchmarkProfile"
    ]
    """<p>The message benchmark profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCisSessionMessage) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.stop_cis_session_status

    out["status"] = aws_sdk_inspector2.types.stop_cis_session_status.serialize_json(
        value["status"]
    )
    if "reason" in value:
        out["reason"] = value["reason"]
    import aws_sdk_inspector2.types.stop_cis_message_progress

    out["progress"] = aws_sdk_inspector2.types.stop_cis_message_progress.serialize_json(
        value["progress"]
    )
    if "compute_platform" in value:
        import aws_sdk_inspector2.types.compute_platform

        out["computePlatform"] = (
            aws_sdk_inspector2.types.compute_platform.serialize_json(
                value["compute_platform"]
            )
        )
    if "benchmark_version" in value:
        out["benchmarkVersion"] = value["benchmark_version"]
    if "benchmark_profile" in value:
        out["benchmarkProfile"] = value["benchmark_profile"]
    return out


def deserialize_json(data: dict) -> StopCisSessionMessage:
    out: StopCisSessionMessage = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_inspector2.types.stop_cis_session_status

        out["status"] = (
            aws_sdk_inspector2.types.stop_cis_session_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StopCisSessionMessage.status required")
    if "reason" in data:
        out["reason"] = data["reason"]
    if "progress" in data:
        import aws_sdk_inspector2.types.stop_cis_message_progress

        out["progress"] = (
            aws_sdk_inspector2.types.stop_cis_message_progress.deserialize_json(
                data["progress"]
            )
        )
    else:
        raise DeserializationError("StopCisSessionMessage.progress required")
    if "computePlatform" in data:
        import aws_sdk_inspector2.types.compute_platform

        out["compute_platform"] = (
            aws_sdk_inspector2.types.compute_platform.deserialize_json(
                data["computePlatform"]
            )
        )
    if "benchmarkVersion" in data:
        out["benchmark_version"] = data["benchmarkVersion"]
    if "benchmarkProfile" in data:
        out["benchmark_profile"] = data["benchmarkProfile"]
    return out
