"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateAppBlockBuilderAppBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.name


class AssociateAppBlockBuilderAppBlockRequest(TypedDict):
    app_block_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the app block.</p>"""
    app_block_builder_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the app block builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateAppBlockBuilderAppBlockRequest) -> dict:
    out: dict = {}
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateAppBlockBuilderAppBlockRequest:
    out: AssociateAppBlockBuilderAppBlockRequest = {}  # type: ignore[typeddict-item]
    if "AppBlockArn" in data:
        out["app_block_arn"] = data["AppBlockArn"]
    if "AppBlockBuilderName" in data:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    return out
