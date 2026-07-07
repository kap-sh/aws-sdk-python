"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyDiscoveryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.dependency_discovery_status


class DependencyDiscoveryConfig(TypedDict, closed=True):
    status: "aws_sdk_resiliencehubv2.types.dependency_discovery_status.DependencyDiscoveryStatus"
    """<p>The current status of dependency discovery.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when dependency discovery was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyDiscoveryConfig) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.dependency_discovery_status

    out["status"] = (
        aws_sdk_resiliencehubv2.types.dependency_discovery_status.serialize_json(
            value["status"]
        )
    )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> DependencyDiscoveryConfig:
    out: DependencyDiscoveryConfig = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_resiliencehubv2.types.dependency_discovery_status

        out["status"] = (
            aws_sdk_resiliencehubv2.types.dependency_discovery_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DependencyDiscoveryConfig.status required")
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
