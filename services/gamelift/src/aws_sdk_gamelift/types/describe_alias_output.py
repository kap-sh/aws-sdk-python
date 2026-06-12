"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeAliasOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.alias


class DescribeAliasOutput(TypedDict):
    alias: NotRequired["aws_sdk_gamelift.types.alias.Alias"]
    """<p>The requested alias resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAliasOutput) -> dict:
    out: dict = {}
    if "alias" in value:
        import aws_sdk_gamelift.types.alias

        out["Alias"] = aws_sdk_gamelift.types.alias.serialize_aws_json_1_1(
            value["alias"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAliasOutput:
    out: DescribeAliasOutput = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        import aws_sdk_gamelift.types.alias

        out["alias"] = aws_sdk_gamelift.types.alias.deserialize_aws_json_1_1(
            data["Alias"]
        )
    return out
