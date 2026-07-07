"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RegionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.region_status
    import aws_sdk_ssm_incidents.types.sse_kms_key


class RegionInfo(TypedDict, closed=True):
    sse_kms_key_id: NotRequired["aws_sdk_ssm_incidents.types.sse_kms_key.SseKmsKey"]
    """<p>The ID of the KMS key used to encrypt the data in this Amazon Web Services Region.</p>"""
    status: "aws_sdk_ssm_incidents.types.region_status.RegionStatus"
    """<p>The status of the Amazon Web Services Region in the replication set.</p>"""
    status_message: NotRequired["str"]
    """<p>Information displayed about the status of the Amazon Web Services Region.</p>"""
    status_update_date_time: "datetime.datetime"
    """<p>The timestamp for when Incident Manager updated the status of the Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionInfo) -> dict:
    out: dict = {}
    if "sse_kms_key_id" in value:
        out["sseKmsKeyId"] = value["sse_kms_key_id"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["statusUpdateDateTime"] = (
        aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["status_update_date_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegionInfo:
    out: RegionInfo = {}  # type: ignore[typeddict-item]
    if "sseKmsKeyId" in data:
        out["sse_kms_key_id"] = data["sseKmsKeyId"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("RegionInfo.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "statusUpdateDateTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["status_update_date_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["statusUpdateDateTime"]
            )
        )
    else:
        raise DeserializationError("RegionInfo.status_update_date_time required")
    return out
