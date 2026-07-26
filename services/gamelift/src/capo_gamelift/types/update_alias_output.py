"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.alias


class UpdateAliasOutput(TypedDict, closed=True):
    alias: NotRequired["capo_gamelift.types.alias.Alias"]
    """<p>The updated alias resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAliasOutput) -> dict:
    out: dict = {}
    if "alias" in value:
        import capo_gamelift.types.alias

        out["Alias"] = capo_gamelift.types.alias.serialize_aws_json_1_1(value["alias"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAliasOutput:
    out: UpdateAliasOutput = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        import capo_gamelift.types.alias

        out["alias"] = capo_gamelift.types.alias.deserialize_aws_json_1_1(data["Alias"])
    return out
