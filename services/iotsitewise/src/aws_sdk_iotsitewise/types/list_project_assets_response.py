"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListProjectAssetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_i_ds
    import aws_sdk_iotsitewise.types.next_token


class ListProjectAssetsResponse(TypedDict):
    asset_ids: "aws_sdk_iotsitewise.types.asset_i_ds.AssetIDs"
    """<p>A list that contains the IDs of each asset associated with the project.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectAssetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_i_ds

    out["assetIds"] = aws_sdk_iotsitewise.types.asset_i_ds.serialize_json(
        value["asset_ids"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectAssetsResponse:
    out: ListProjectAssetsResponse = {}  # type: ignore[typeddict-item]
    if "assetIds" in data:
        import aws_sdk_iotsitewise.types.asset_i_ds

        out["asset_ids"] = aws_sdk_iotsitewise.types.asset_i_ds.deserialize_json(
            data["assetIds"]
        )
    else:
        raise DeserializationError("ListProjectAssetsResponse.asset_ids required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
