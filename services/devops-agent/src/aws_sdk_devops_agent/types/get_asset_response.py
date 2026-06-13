"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset


class GetAssetResponse(TypedDict):
    asset: "aws_sdk_devops_agent.types.asset.Asset"
    """<p>The asset object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.asset

    out["asset"] = aws_sdk_devops_agent.types.asset.serialize_json(value["asset"])
    return out


def deserialize_json(data: dict) -> GetAssetResponse:
    out: GetAssetResponse = {}  # type: ignore[typeddict-item]
    if "asset" in data:
        import aws_sdk_devops_agent.types.asset

        out["asset"] = aws_sdk_devops_agent.types.asset.deserialize_json(data["asset"])
    else:
        raise DeserializationError("GetAssetResponse.asset required")
    return out
