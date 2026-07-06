"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.alias


class CreateAliasOutput(TypedDict, closed=True):
    alias: NotRequired["aws_sdk_gamelift.types.alias.Alias"]
    """<p>The newly created alias resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAliasOutput) -> dict:
    out: dict = {}
    if "alias" in value:
        import aws_sdk_gamelift.types.alias

        out["Alias"] = aws_sdk_gamelift.types.alias.serialize_aws_json_1_1(
            value["alias"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAliasOutput:
    out: CreateAliasOutput = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        import aws_sdk_gamelift.types.alias

        out["alias"] = aws_sdk_gamelift.types.alias.deserialize_aws_json_1_1(
            data["Alias"]
        )
    return out
