"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceSharingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.sharing_type


class SpaceSharingSettings(TypedDict):
    sharing_type: NotRequired["aws_sdk_sagemaker.types.sharing_type.SharingType"]
    """<p>Specifies the sharing type of the space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceSharingSettings) -> dict:
    out: dict = {}
    if "sharing_type" in value:
        import aws_sdk_sagemaker.types.sharing_type

        out["SharingType"] = (
            aws_sdk_sagemaker.types.sharing_type.serialize_aws_json_1_1(
                value["sharing_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceSharingSettings:
    out: SpaceSharingSettings = {}  # type: ignore[typeddict-item]
    if "SharingType" in data:
        import aws_sdk_sagemaker.types.sharing_type

        out["sharing_type"] = (
            aws_sdk_sagemaker.types.sharing_type.deserialize_aws_json_1_1(
                data["SharingType"]
            )
        )
    return out
