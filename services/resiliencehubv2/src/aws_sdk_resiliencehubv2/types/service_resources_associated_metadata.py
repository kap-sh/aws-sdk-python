"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceResourcesAssociatedMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.resource_type_list


class ServiceResourcesAssociatedMetadata(TypedDict):
    resource_count: NotRequired["int"]
    """<p>The number of resources associated.</p>"""
    resource_types: NotRequired[
        "aws_sdk_resiliencehubv2.types.resource_type_list.ResourceTypeList"
    ]
    """<p>The types of resources associated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourcesAssociatedMetadata) -> dict:
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


def deserialize_json(data: dict) -> ServiceResourcesAssociatedMetadata:
    out: ServiceResourcesAssociatedMetadata = {}  # type: ignore[typeddict-item]
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
