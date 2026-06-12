"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlockBuilderStreamingURLRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.long
    import aws_sdk_appstream.types.name


class CreateAppBlockBuilderStreamingURLRequest(TypedDict):
    app_block_builder_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the app block builder.</p>"""
    validity: NotRequired["aws_sdk_appstream.types.long.Long"]
    """<p>The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppBlockBuilderStreamingURLRequest) -> dict:
    out: dict = {}
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    if "validity" in value:
        out["Validity"] = value["validity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppBlockBuilderStreamingURLRequest:
    out: CreateAppBlockBuilderStreamingURLRequest = {}  # type: ignore[typeddict-item]
    if "AppBlockBuilderName" in data:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    if "Validity" in data:
        out["validity"] = data["Validity"]
    return out
