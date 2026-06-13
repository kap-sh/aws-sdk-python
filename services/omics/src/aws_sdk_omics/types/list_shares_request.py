"""Generated from Smithy shape ``com.amazonaws.omics#ListSharesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.filter
    import aws_sdk_omics.types.resource_owner


class ListSharesRequest(TypedDict):
    resource_owner: "aws_sdk_omics.types.resource_owner.ResourceOwner"
    """<p>The account that owns the resource shares.</p>"""
    filter: NotRequired["aws_sdk_omics.types.filter.Filter"]
    """<p>Attributes that you use to filter for a specific subset of resource shares.</p>"""
    next_token: NotRequired["str"]
    """<p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of shares to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSharesRequest) -> dict:
    out: dict = {}
    out["resourceOwner"] = value["resource_owner"]
    if "filter" in value:
        import aws_sdk_omics.types.filter

        out["filter"] = aws_sdk_omics.types.filter.serialize_json(value["filter"])
    return out


def deserialize_json(data: dict) -> ListSharesRequest:
    out: ListSharesRequest = {}  # type: ignore[typeddict-item]
    if "resourceOwner" in data:
        out["resource_owner"] = data["resourceOwner"]
    else:
        raise DeserializationError("ListSharesRequest.resource_owner required")
    if "filter" in data:
        import aws_sdk_omics.types.filter

        out["filter"] = aws_sdk_omics.types.filter.deserialize_json(data["filter"])
    return out
