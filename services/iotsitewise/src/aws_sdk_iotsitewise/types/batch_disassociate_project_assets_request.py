"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchDisassociateProjectAssetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.i_ds
    import aws_sdk_iotsitewise.types.id


class BatchDisassociateProjectAssetsRequest(TypedDict, closed=True):
    project_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project from which to disassociate the assets.</p>"""
    asset_ids: "aws_sdk_iotsitewise.types.i_ds.IDs"
    """<p>The IDs of the assets to be disassociated from the project.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateProjectAssetsRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.i_ds

    out["assetIds"] = aws_sdk_iotsitewise.types.i_ds.serialize_json(value["asset_ids"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchDisassociateProjectAssetsRequest:
    out: BatchDisassociateProjectAssetsRequest = {}  # type: ignore[typeddict-item]
    if "assetIds" in data:
        import aws_sdk_iotsitewise.types.i_ds

        out["asset_ids"] = aws_sdk_iotsitewise.types.i_ds.deserialize_json(
            data["assetIds"]
        )
    else:
        raise DeserializationError(
            "BatchDisassociateProjectAssetsRequest.asset_ids required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
