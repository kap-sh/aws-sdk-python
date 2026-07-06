"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.ota_update_arn
    import aws_sdk_iot.types.ota_update_id


class OTAUpdateSummary(TypedDict, closed=True):
    ota_update_id: NotRequired["aws_sdk_iot.types.ota_update_id.OTAUpdateId"]
    """<p>The OTA update ID.</p>"""
    ota_update_arn: NotRequired["aws_sdk_iot.types.ota_update_arn.OTAUpdateArn"]
    """<p>The OTA update ARN.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the OTA update was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdateSummary) -> dict:
    out: dict = {}
    if "ota_update_id" in value:
        out["otaUpdateId"] = value["ota_update_id"]
    if "ota_update_arn" in value:
        out["otaUpdateArn"] = value["ota_update_arn"]
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> OTAUpdateSummary:
    out: OTAUpdateSummary = {}  # type: ignore[typeddict-item]
    if "otaUpdateId" in data:
        out["ota_update_id"] = data["otaUpdateId"]
    if "otaUpdateArn" in data:
        out["ota_update_arn"] = data["otaUpdateArn"]
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    return out
