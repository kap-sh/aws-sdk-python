"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlockBuilderResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_block_builder


class CreateAppBlockBuilderResult(TypedDict):
    app_block_builder: NotRequired[
        "aws_sdk_appstream.types.app_block_builder.AppBlockBuilder"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppBlockBuilderResult) -> dict:
    out: dict = {}
    if "app_block_builder" in value:
        import aws_sdk_appstream.types.app_block_builder

        out["AppBlockBuilder"] = (
            aws_sdk_appstream.types.app_block_builder.serialize_aws_json_1_1(
                value["app_block_builder"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppBlockBuilderResult:
    out: CreateAppBlockBuilderResult = {}  # type: ignore[typeddict-item]
    if "AppBlockBuilder" in data:
        import aws_sdk_appstream.types.app_block_builder

        out["app_block_builder"] = (
            aws_sdk_appstream.types.app_block_builder.deserialize_aws_json_1_1(
                data["AppBlockBuilder"]
            )
        )
    return out
