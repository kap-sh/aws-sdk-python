"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AnalyzableServerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.string


class AnalyzableServerSummary(TypedDict, closed=True):
    hostname: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """The host name of the analyzable server."""
    ip_address: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """The ip address of the analyzable server."""
    source: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """The data source of the analyzable server."""
    vm_id: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """The virtual machine id of the analyzable server."""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzableServerSummary) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "source" in value:
        out["source"] = value["source"]
    if "vm_id" in value:
        out["vmId"] = value["vm_id"]
    return out


def deserialize_json(data: dict) -> AnalyzableServerSummary:
    out: AnalyzableServerSummary = {}  # type: ignore[typeddict-item]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "source" in data:
        out["source"] = data["source"]
    if "vmId" in data:
        out["vm_id"] = data["vmId"]
    return out
