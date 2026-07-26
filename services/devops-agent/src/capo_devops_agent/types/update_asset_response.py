"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.asset


class UpdateAssetResponse(TypedDict, closed=True):
    asset: "capo_devops_agent.types.asset.Asset"
    """<p>The asset object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.asset

    out["asset"] = capo_devops_agent.types.asset.serialize_json(value["asset"])
    return out


def deserialize_json(data: dict) -> UpdateAssetResponse:
    out: UpdateAssetResponse = {}  # type: ignore[typeddict-item]
    if "asset" in data:
        import capo_devops_agent.types.asset

        out["asset"] = capo_devops_agent.types.asset.deserialize_json(data["asset"])
    else:
        raise DeserializationError("UpdateAssetResponse.asset required")
    return out
