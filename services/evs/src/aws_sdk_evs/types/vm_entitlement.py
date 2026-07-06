"""Generated from Smithy shape ``com.amazonaws.evs#VmEntitlement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_evs.types.connector_id
    import aws_sdk_evs.types.entitlement_status
    import aws_sdk_evs.types.entitlement_type
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.error_detail
    import aws_sdk_evs.types.vm_id
    import aws_sdk_evs.types.vm_name


class VmEntitlement(TypedDict, closed=True):
    vm_id: NotRequired["aws_sdk_evs.types.vm_id.VmId"]
    """<p>The unique ID of the virtual machine.</p>"""
    environment_id: NotRequired["aws_sdk_evs.types.environment_id.EnvironmentId"]
    """<p>The unique ID of the environment.</p>"""
    connector_id: NotRequired["aws_sdk_evs.types.connector_id.ConnectorId"]
    """<p>The unique ID of the connector associated with the entitlement.</p>"""
    vm_name: NotRequired["aws_sdk_evs.types.vm_name.VmName"]
    """<p>The name of the virtual machine.</p>"""
    type: NotRequired["aws_sdk_evs.types.entitlement_type.EntitlementType"]
    """<p>The type of entitlement.</p>"""
    status: NotRequired["aws_sdk_evs.types.entitlement_status.EntitlementStatus"]
    """<p>The status of the entitlement.</p>"""
    last_synced_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the entitlement was last synced.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the entitlement started.</p>"""
    stopped_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the entitlement stopped.</p>"""
    error_detail: NotRequired["aws_sdk_evs.types.error_detail.ErrorDetail"]
    """<p>The error details associated with the entitlement, if applicable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmEntitlement) -> dict:
    out: dict = {}
    if "vm_id" in value:
        out["vmId"] = value["vm_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "connector_id" in value:
        out["connectorId"] = value["connector_id"]
    if "vm_name" in value:
        out["vmName"] = value["vm_name"]
    if "type" in value:
        import aws_sdk_evs.types.entitlement_type

        out["type"] = aws_sdk_evs.types.entitlement_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_evs.types.entitlement_status

        out["status"] = aws_sdk_evs.types.entitlement_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "last_synced_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["lastSyncedAt"] = (
            aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_synced_at"]
            )
        )
    if "started_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["startedAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["started_at"]
        )
    if "stopped_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["stoppedAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["stopped_at"]
        )
    if "error_detail" in value:
        import aws_sdk_evs.types.error_detail

        out["errorDetail"] = aws_sdk_evs.types.error_detail.serialize_aws_json_1_0(
            value["error_detail"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VmEntitlement:
    out: VmEntitlement = {}  # type: ignore[typeddict-item]
    if "vmId" in data:
        out["vm_id"] = data["vmId"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "connectorId" in data:
        out["connector_id"] = data["connectorId"]
    if "vmName" in data:
        out["vm_name"] = data["vmName"]
    if "type" in data:
        import aws_sdk_evs.types.entitlement_type

        out["type"] = aws_sdk_evs.types.entitlement_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if "status" in data:
        import aws_sdk_evs.types.entitlement_status

        out["status"] = aws_sdk_evs.types.entitlement_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "lastSyncedAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["last_synced_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastSyncedAt"]
            )
        )
    if "startedAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["started_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startedAt"]
            )
        )
    if "stoppedAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["stopped_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["stoppedAt"]
            )
        )
    if "errorDetail" in data:
        import aws_sdk_evs.types.error_detail

        out["error_detail"] = aws_sdk_evs.types.error_detail.deserialize_aws_json_1_0(
            data["errorDetail"]
        )
    return out
