"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputSecurityGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListInputSecurityGroupsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputSecurityGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInputSecurityGroupsRequest:
    out: ListInputSecurityGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
