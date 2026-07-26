"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceSystemAssociatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class ServiceSystemAssociatedMetadata(TypedDict, closed=True):
    system_name: NotRequired["str"]
    """<p>The name of the associated system.</p>"""
    system_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSystemAssociatedMetadata) -> dict:
    out: dict = {}
    if "system_name" in value:
        out["systemName"] = value["system_name"]
    if "system_arn" in value:
        out["systemArn"] = value["system_arn"]
    return out


def deserialize_json(data: dict) -> ServiceSystemAssociatedMetadata:
    out: ServiceSystemAssociatedMetadata = {}  # type: ignore[typeddict-item]
    if "systemName" in data:
        out["system_name"] = data["systemName"]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    return out
