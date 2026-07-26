"""Generated from Smithy shape ``com.amazonaws.appstream#StopAppBlockBuilderResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder


class StopAppBlockBuilderResult(TypedDict, closed=True):
    app_block_builder: NotRequired[
        "capo_appstream.types.app_block_builder.AppBlockBuilder"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAppBlockBuilderResult) -> dict:
    out: dict = {}
    if "app_block_builder" in value:
        import capo_appstream.types.app_block_builder

        out["AppBlockBuilder"] = (
            capo_appstream.types.app_block_builder.serialize_aws_json_1_1(
                value["app_block_builder"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAppBlockBuilderResult:
    out: StopAppBlockBuilderResult = {}  # type: ignore[typeddict-item]
    if "AppBlockBuilder" in data:
        import capo_appstream.types.app_block_builder

        out["app_block_builder"] = (
            capo_appstream.types.app_block_builder.deserialize_aws_json_1_1(
                data["AppBlockBuilder"]
            )
        )
    return out
