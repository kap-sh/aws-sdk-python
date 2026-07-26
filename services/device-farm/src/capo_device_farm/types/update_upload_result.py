"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateUploadResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.upload


class UpdateUploadResult(TypedDict, closed=True):
    upload: NotRequired["capo_device_farm.types.upload.Upload"]
    """<p>A test spec uploaded to Device Farm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUploadResult) -> dict:
    out: dict = {}
    if "upload" in value:
        import capo_device_farm.types.upload

        out["upload"] = capo_device_farm.types.upload.serialize_aws_json_1_1(
            value["upload"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUploadResult:
    out: UpdateUploadResult = {}  # type: ignore[typeddict-item]
    if "upload" in data:
        import capo_device_farm.types.upload

        out["upload"] = capo_device_farm.types.upload.deserialize_aws_json_1_1(
            data["upload"]
        )
    return out
