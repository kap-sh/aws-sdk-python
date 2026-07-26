"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppVersionResourceMappingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.resource_mapping_list


class ListAppVersionResourceMappingsResponse(TypedDict, closed=True):
    resource_mappings: (
        "capo_resiliencehub.types.resource_mapping_list.ResourceMappingList"
    )
    """<p>Mappings used to map logical resources from the template to physical resources. You can use the mapping type <code>CFN_STACK</code> if the application template uses a logical stack name. Or you can map individual resources by using the mapping type <code>RESOURCE</code>. We recommend using the mapping type <code>CFN_STACK</code> if the application is backed by a CloudFormation stack.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppVersionResourceMappingsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.resource_mapping_list

    out["resourceMappings"] = (
        capo_resiliencehub.types.resource_mapping_list.serialize_json(
            value["resource_mappings"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppVersionResourceMappingsResponse:
    out: ListAppVersionResourceMappingsResponse = {}  # type: ignore[typeddict-item]
    if "resourceMappings" in data:
        import capo_resiliencehub.types.resource_mapping_list

        out["resource_mappings"] = (
            capo_resiliencehub.types.resource_mapping_list.deserialize_json(
                data["resourceMappings"]
            )
        )
    else:
        raise DeserializationError(
            "ListAppVersionResourceMappingsResponse.resource_mappings required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
