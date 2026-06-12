"""Generated from Smithy shape ``com.amazonaws.snowball#TargetOnDeviceService``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.device_service_name
    import aws_sdk_snowball.types.transfer_option


class TargetOnDeviceService(TypedDict):
    service_name: NotRequired[
        "aws_sdk_snowball.types.device_service_name.DeviceServiceName"
    ]
    """<p>Specifies the name of the service on the Snow Family device that your transferred data will be exported from or imported into.</p>"""
    transfer_option: NotRequired[
        "aws_sdk_snowball.types.transfer_option.TransferOption"
    ]
    """<p>Specifies whether the data is being imported or exported. You can import or export the data, or use it locally on the device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetOnDeviceService) -> dict:
    out: dict = {}
    if "service_name" in value:
        import aws_sdk_snowball.types.device_service_name

        out["ServiceName"] = (
            aws_sdk_snowball.types.device_service_name.serialize_aws_json_1_1(
                value["service_name"]
            )
        )
    if "transfer_option" in value:
        import aws_sdk_snowball.types.transfer_option

        out["TransferOption"] = (
            aws_sdk_snowball.types.transfer_option.serialize_aws_json_1_1(
                value["transfer_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetOnDeviceService:
    out: TargetOnDeviceService = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        import aws_sdk_snowball.types.device_service_name

        out["service_name"] = (
            aws_sdk_snowball.types.device_service_name.deserialize_aws_json_1_1(
                data["ServiceName"]
            )
        )
    if "TransferOption" in data:
        import aws_sdk_snowball.types.transfer_option

        out["transfer_option"] = (
            aws_sdk_snowball.types.transfer_option.deserialize_aws_json_1_1(
                data["TransferOption"]
            )
        )
    return out
