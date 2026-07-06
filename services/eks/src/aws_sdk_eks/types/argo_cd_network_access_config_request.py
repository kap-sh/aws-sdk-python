"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdNetworkAccessConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string_list


class ArgoCdNetworkAccessConfigRequest(TypedDict, closed=True):
    vpce_ids: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>A list of VPC endpoint IDs to associate with the managed Argo CD API server endpoint. Each VPC endpoint provides private connectivity from a specific VPC to the Argo CD server. You can specify multiple VPC endpoint IDs to enable access from multiple VPCs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdNetworkAccessConfigRequest) -> dict:
    out: dict = {}
    if "vpce_ids" in value:
        import aws_sdk_eks.types.string_list

        out["vpceIds"] = aws_sdk_eks.types.string_list.serialize_json(value["vpce_ids"])
    return out


def deserialize_json(data: dict) -> ArgoCdNetworkAccessConfigRequest:
    out: ArgoCdNetworkAccessConfigRequest = {}  # type: ignore[typeddict-item]
    if "vpceIds" in data:
        import aws_sdk_eks.types.string_list

        out["vpce_ids"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["vpceIds"]
        )
    return out
