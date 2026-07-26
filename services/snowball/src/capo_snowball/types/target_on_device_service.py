"""Generated from Smithy shape ``com.amazonaws.snowball#TargetOnDeviceService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.device_service_name
    import capo_snowball.types.transfer_option


class TargetOnDeviceService(TypedDict, closed=True):
    service_name: NotRequired[
        "capo_snowball.types.device_service_name.DeviceServiceName"
    ]
    """<p>Specifies the name of the service on the Snow Family device that your transferred data will be exported from or imported into.</p>"""
    transfer_option: NotRequired["capo_snowball.types.transfer_option.TransferOption"]
    """<p>Specifies whether the data is being imported or exported. You can import or export the data, or use it locally on the device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetOnDeviceService) -> dict:
    out: dict = {}
    if "service_name" in value:
        import capo_snowball.types.device_service_name

        out["ServiceName"] = (
            capo_snowball.types.device_service_name.serialize_aws_json_1_1(
                value["service_name"]
            )
        )
    if "transfer_option" in value:
        import capo_snowball.types.transfer_option

        out["TransferOption"] = (
            capo_snowball.types.transfer_option.serialize_aws_json_1_1(
                value["transfer_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetOnDeviceService:
    out: TargetOnDeviceService = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        import capo_snowball.types.device_service_name

        out["service_name"] = (
            capo_snowball.types.device_service_name.deserialize_aws_json_1_1(
                data["ServiceName"]
            )
        )
    if "TransferOption" in data:
        import capo_snowball.types.transfer_option

        out["transfer_option"] = (
            capo_snowball.types.transfer_option.deserialize_aws_json_1_1(
                data["TransferOption"]
            )
        )
    return out
