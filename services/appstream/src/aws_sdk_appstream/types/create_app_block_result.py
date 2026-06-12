"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlockResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_block


class CreateAppBlockResult(TypedDict):
    app_block: NotRequired["aws_sdk_appstream.types.app_block.AppBlock"]
    """<p>The app block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppBlockResult) -> dict:
    out: dict = {}
    if "app_block" in value:
        import aws_sdk_appstream.types.app_block

        out["AppBlock"] = aws_sdk_appstream.types.app_block.serialize_aws_json_1_1(
            value["app_block"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppBlockResult:
    out: CreateAppBlockResult = {}  # type: ignore[typeddict-item]
    if "AppBlock" in data:
        import aws_sdk_appstream.types.app_block

        out["app_block"] = aws_sdk_appstream.types.app_block.deserialize_aws_json_1_1(
            data["AppBlock"]
        )
    return out
