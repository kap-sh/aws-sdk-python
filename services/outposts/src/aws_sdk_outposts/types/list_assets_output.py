"""Generated from Smithy shape ``com.amazonaws.outposts#ListAssetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_list_definition
    import aws_sdk_outposts.types.token


class ListAssetsOutput(TypedDict, closed=True):
    assets: NotRequired[
        "aws_sdk_outposts.types.asset_list_definition.AssetListDefinition"
    ]
    """<p>Information about the hardware assets.</p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsOutput) -> dict:
    out: dict = {}
    if "assets" in value:
        import aws_sdk_outposts.types.asset_list_definition

        out["Assets"] = aws_sdk_outposts.types.asset_list_definition.serialize_json(
            value["assets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetsOutput:
    out: ListAssetsOutput = {}  # type: ignore[typeddict-item]
    if "Assets" in data:
        import aws_sdk_outposts.types.asset_list_definition

        out["assets"] = aws_sdk_outposts.types.asset_list_definition.deserialize_json(
            data["Assets"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
