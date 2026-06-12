"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateBuildOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build


class UpdateBuildOutput(TypedDict):
    build: NotRequired["aws_sdk_gamelift.types.build.Build"]
    """<p>The updated build resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import aws_sdk_gamelift.types.build

        out["Build"] = aws_sdk_gamelift.types.build.serialize_aws_json_1_1(
            value["build"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBuildOutput:
    out: UpdateBuildOutput = {}  # type: ignore[typeddict-item]
    if "Build" in data:
        import aws_sdk_gamelift.types.build

        out["build"] = aws_sdk_gamelift.types.build.deserialize_aws_json_1_1(
            data["Build"]
        )
    return out
