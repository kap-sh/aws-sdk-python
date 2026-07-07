"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceDiscoveryStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.resource_discovery_error_code
    import aws_sdk_resiliencehubv2.types.resource_discovery_run_status


class ResourceDiscoveryStatus(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_resiliencehubv2.types.resource_discovery_run_status.ResourceDiscoveryRunStatus"
    ]
    """<p>The current status of resource discovery.</p>"""
    last_run_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of the last resource discovery run.</p>"""
    error_code: NotRequired[
        "aws_sdk_resiliencehubv2.types.resource_discovery_error_code.ResourceDiscoveryErrorCode"
    ]
    """<p>The error code if resource discovery failed.</p>"""
    error_message: NotRequired["str"]
    """<p>A message describing the error if resource discovery failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDiscoveryStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_resiliencehubv2.types.resource_discovery_run_status

        out["status"] = (
            aws_sdk_resiliencehubv2.types.resource_discovery_run_status.serialize_json(
                value["status"]
            )
        )
    if "last_run_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["lastRunAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["last_run_at"]
            )
        )
    if "error_code" in value:
        import aws_sdk_resiliencehubv2.types.resource_discovery_error_code

        out["errorCode"] = (
            aws_sdk_resiliencehubv2.types.resource_discovery_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ResourceDiscoveryStatus:
    out: ResourceDiscoveryStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_resiliencehubv2.types.resource_discovery_run_status

        out["status"] = (
            aws_sdk_resiliencehubv2.types.resource_discovery_run_status.deserialize_json(
                data["status"]
            )
        )
    if "lastRunAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["last_run_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["lastRunAt"]
            )
        )
    if "errorCode" in data:
        import aws_sdk_resiliencehubv2.types.resource_discovery_error_code

        out["error_code"] = (
            aws_sdk_resiliencehubv2.types.resource_discovery_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
