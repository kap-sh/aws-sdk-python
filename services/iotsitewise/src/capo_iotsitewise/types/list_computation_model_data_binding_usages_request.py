"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListComputationModelDataBindingUsagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_binding_value_filter
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListComputationModelDataBindingUsagesRequest(TypedDict, closed=True):
    data_binding_value_filter: (
        "capo_iotsitewise.types.data_binding_value_filter.DataBindingValueFilter"
    )
    """<p>A filter used to limit the returned data binding usages based on specific data binding values. You can filter by asset, asset model, asset property, or asset model property to find all computation models using these specific data sources.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results returned for each paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComputationModelDataBindingUsagesRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.data_binding_value_filter

    out["dataBindingValueFilter"] = (
        capo_iotsitewise.types.data_binding_value_filter.serialize_json(
            value["data_binding_value_filter"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListComputationModelDataBindingUsagesRequest:
    out: ListComputationModelDataBindingUsagesRequest = {}  # type: ignore[typeddict-item]
    if "dataBindingValueFilter" in data:
        import capo_iotsitewise.types.data_binding_value_filter

        out["data_binding_value_filter"] = (
            capo_iotsitewise.types.data_binding_value_filter.deserialize_json(
                data["dataBindingValueFilter"]
            )
        )
    else:
        raise DeserializationError(
            "ListComputationModelDataBindingUsagesRequest.data_binding_value_filter required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
