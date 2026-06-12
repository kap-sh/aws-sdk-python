"""Generated from Smithy shape ``com.amazonaws.xray#PutTelemetryRecordsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.ec2_instance_id
    import aws_sdk_xray.types.hostname
    import aws_sdk_xray.types.resource_arn
    import aws_sdk_xray.types.telemetry_record_list


class PutTelemetryRecordsRequest(TypedDict):
    telemetry_records: "aws_sdk_xray.types.telemetry_record_list.TelemetryRecordList"
    """<p></p>"""
    ec2_instance_id: NotRequired["aws_sdk_xray.types.ec2_instance_id.EC2InstanceId"]
    """<p></p>"""
    hostname: NotRequired["aws_sdk_xray.types.hostname.Hostname"]
    """<p></p>"""
    resource_arn: NotRequired["aws_sdk_xray.types.resource_arn.ResourceARN"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTelemetryRecordsRequest) -> dict:
    out: dict = {}
    import aws_sdk_xray.types.telemetry_record_list

    out["TelemetryRecords"] = aws_sdk_xray.types.telemetry_record_list.serialize_json(
        value["telemetry_records"]
    )
    if "ec2_instance_id" in value:
        out["EC2InstanceId"] = value["ec2_instance_id"]
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> PutTelemetryRecordsRequest:
    out: PutTelemetryRecordsRequest = {}  # type: ignore[typeddict-item]
    if "TelemetryRecords" in data:
        import aws_sdk_xray.types.telemetry_record_list

        out["telemetry_records"] = (
            aws_sdk_xray.types.telemetry_record_list.deserialize_json(
                data["TelemetryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "PutTelemetryRecordsRequest.telemetry_records required"
        )
    if "EC2InstanceId" in data:
        out["ec2_instance_id"] = data["EC2InstanceId"]
    if "Hostname" in data:
        out["hostname"] = data["Hostname"]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    return out
