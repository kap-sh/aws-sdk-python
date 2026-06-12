"""Generated from Smithy shape ``com.amazonaws.xray#AnomalousService``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.service_id


class AnomalousService(TypedDict):
    service_id: NotRequired["aws_sdk_xray.types.service_id.ServiceId"]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalousService) -> dict:
    out: dict = {}
    if "service_id" in value:
        import aws_sdk_xray.types.service_id

        out["ServiceId"] = aws_sdk_xray.types.service_id.serialize_json(
            value["service_id"]
        )
    return out


def deserialize_json(data: dict) -> AnomalousService:
    out: AnomalousService = {}  # type: ignore[typeddict-item]
    if "ServiceId" in data:
        import aws_sdk_xray.types.service_id

        out["service_id"] = aws_sdk_xray.types.service_id.deserialize_json(
            data["ServiceId"]
        )
    return out
