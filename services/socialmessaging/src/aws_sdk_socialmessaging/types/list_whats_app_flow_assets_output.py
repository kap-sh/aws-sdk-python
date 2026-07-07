"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppFlowAssetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_asset_list
    import aws_sdk_socialmessaging.types.next_token


class ListWhatsAppFlowAssetsOutput(TypedDict, closed=True):
    flow_assets: "aws_sdk_socialmessaging.types.meta_flow_asset_list.MetaFlowAssetList"
    """<p>A list of Flow assets with download URLs.</p>"""
    next_token: NotRequired["aws_sdk_socialmessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppFlowAssetsOutput) -> dict:
    out: dict = {}
    import aws_sdk_socialmessaging.types.meta_flow_asset_list

    out["flowAssets"] = (
        aws_sdk_socialmessaging.types.meta_flow_asset_list.serialize_json(
            value["flow_assets"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWhatsAppFlowAssetsOutput:
    out: ListWhatsAppFlowAssetsOutput = {}  # type: ignore[typeddict-item]
    if "flowAssets" in data:
        import aws_sdk_socialmessaging.types.meta_flow_asset_list

        out["flow_assets"] = (
            aws_sdk_socialmessaging.types.meta_flow_asset_list.deserialize_json(
                data["flowAssets"]
            )
        )
    else:
        raise DeserializationError("ListWhatsAppFlowAssetsOutput.flow_assets required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
