"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceSystemDisassociatedMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn


class ServiceSystemDisassociatedMetadata(TypedDict):
    system_id: NotRequired["str"]
    """<p>The identifier of the disassociated system.</p>"""
    system_name: NotRequired["str"]
    """<p>The name of the disassociated system.</p>"""
    system_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSystemDisassociatedMetadata) -> dict:
    out: dict = {}
    if "system_id" in value:
        out["systemId"] = value["system_id"]
    if "system_name" in value:
        out["systemName"] = value["system_name"]
    if "system_arn" in value:
        out["systemArn"] = value["system_arn"]
    return out


def deserialize_json(data: dict) -> ServiceSystemDisassociatedMetadata:
    out: ServiceSystemDisassociatedMetadata = {}  # type: ignore[typeddict-item]
    if "systemId" in data:
        out["system_id"] = data["systemId"]
    if "systemName" in data:
        out["system_name"] = data["systemName"]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    return out
