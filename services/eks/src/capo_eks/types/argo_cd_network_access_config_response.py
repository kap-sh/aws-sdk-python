"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdNetworkAccessConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string_list


class ArgoCdNetworkAccessConfigResponse(TypedDict, closed=True):
    vpce_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The list of VPC endpoint IDs associated with the managed Argo CD API server endpoint. Each VPC endpoint provides private connectivity from a specific VPC to the Argo CD server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdNetworkAccessConfigResponse) -> dict:
    out: dict = {}
    if "vpce_ids" in value:
        import capo_eks.types.string_list

        out["vpceIds"] = capo_eks.types.string_list.serialize_json(value["vpce_ids"])
    return out


def deserialize_json(data: dict) -> ArgoCdNetworkAccessConfigResponse:
    out: ArgoCdNetworkAccessConfigResponse = {}  # type: ignore[typeddict-item]
    if "vpceIds" in data:
        import capo_eks.types.string_list

        out["vpce_ids"] = capo_eks.types.string_list.deserialize_json(data["vpceIds"])
    return out
