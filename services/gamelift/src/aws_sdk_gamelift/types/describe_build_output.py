"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeBuildOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build


class DescribeBuildOutput(TypedDict):
    build: NotRequired["aws_sdk_gamelift.types.build.Build"]
    """<p>Set of properties describing the requested build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import aws_sdk_gamelift.types.build

        out["Build"] = aws_sdk_gamelift.types.build.serialize_aws_json_1_1(
            value["build"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBuildOutput:
    out: DescribeBuildOutput = {}  # type: ignore[typeddict-item]
    if "Build" in data:
        import aws_sdk_gamelift.types.build

        out["build"] = aws_sdk_gamelift.types.build.deserialize_aws_json_1_1(
            data["Build"]
        )
    return out
