"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceResourcesDisassociatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.resource_type_list


class ServiceResourcesDisassociatedMetadata(TypedDict, closed=True):
    resource_count: NotRequired["int"]
    """<p>The number of resources disassociated.</p>"""
    resource_types: NotRequired[
        "aws_sdk_resiliencehubv2.types.resource_type_list.ResourceTypeList"
    ]
    """<p>The types of resources disassociated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourcesDisassociatedMetadata) -> dict:
    out: dict = {}
    if "resource_count" in value:
        out["resourceCount"] = value["resource_count"]
    if "resource_types" in value:
        import aws_sdk_resiliencehubv2.types.resource_type_list

        out["resourceTypes"] = (
            aws_sdk_resiliencehubv2.types.resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceResourcesDisassociatedMetadata:
    out: ServiceResourcesDisassociatedMetadata = {}  # type: ignore[typeddict-item]
    if "resourceCount" in data:
        out["resource_count"] = data["resourceCount"]
    if "resourceTypes" in data:
        import aws_sdk_resiliencehubv2.types.resource_type_list

        out["resource_types"] = (
            aws_sdk_resiliencehubv2.types.resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    return out
