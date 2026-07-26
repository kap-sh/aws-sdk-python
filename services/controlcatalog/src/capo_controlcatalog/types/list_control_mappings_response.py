"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListControlMappingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_mappings
    import capo_controlcatalog.types.pagination_token


class ListControlMappingsResponse(TypedDict, closed=True):
    control_mappings: "capo_controlcatalog.types.control_mappings.ControlMappings"
    """<p>The list of control mappings that the ListControlMappings API returns.</p>"""
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlMappingsResponse) -> dict:
    out: dict = {}
    import capo_controlcatalog.types.control_mappings

    out["ControlMappings"] = capo_controlcatalog.types.control_mappings.serialize_json(
        value["control_mappings"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlMappingsResponse:
    out: ListControlMappingsResponse = {}  # type: ignore[typeddict-item]
    if "ControlMappings" in data:
        import capo_controlcatalog.types.control_mappings

        out["control_mappings"] = (
            capo_controlcatalog.types.control_mappings.deserialize_json(
                data["ControlMappings"]
            )
        )
    else:
        raise DeserializationError(
            "ListControlMappingsResponse.control_mappings required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
