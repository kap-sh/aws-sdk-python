"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateUploadResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.upload


class CreateUploadResult(TypedDict):
    upload: NotRequired["aws_sdk_device_farm.types.upload.Upload"]
    """<p>The newly created upload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUploadResult) -> dict:
    out: dict = {}
    if "upload" in value:
        import aws_sdk_device_farm.types.upload

        out["upload"] = aws_sdk_device_farm.types.upload.serialize_aws_json_1_1(
            value["upload"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUploadResult:
    out: CreateUploadResult = {}  # type: ignore[typeddict-item]
    if "upload" in data:
        import aws_sdk_device_farm.types.upload

        out["upload"] = aws_sdk_device_farm.types.upload.deserialize_aws_json_1_1(
            data["upload"]
        )
    return out
