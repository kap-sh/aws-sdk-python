"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetUploadResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.upload


class GetUploadResult(TypedDict, closed=True):
    upload: NotRequired["aws_sdk_device_farm.types.upload.Upload"]
    """<p>An app or a set of one or more tests to upload or that have been uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUploadResult) -> dict:
    out: dict = {}
    if "upload" in value:
        import aws_sdk_device_farm.types.upload

        out["upload"] = aws_sdk_device_farm.types.upload.serialize_aws_json_1_1(
            value["upload"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUploadResult:
    out: GetUploadResult = {}  # type: ignore[typeddict-item]
    if "upload" in data:
        import aws_sdk_device_farm.types.upload

        out["upload"] = aws_sdk_device_farm.types.upload.deserialize_aws_json_1_1(
            data["upload"]
        )
    return out
