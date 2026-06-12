"""Generated from Smithy shape ``com.amazonaws.fis#ListTargetResourceTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.next_token
    import aws_sdk_fis.types.target_resource_type_summary_list


class ListTargetResourceTypesResponse(TypedDict):
    target_resource_types: NotRequired[
        "aws_sdk_fis.types.target_resource_type_summary_list.TargetResourceTypeSummaryList"
    ]
    """<p>The target resource types.</p>"""
    next_token: NotRequired["aws_sdk_fis.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetResourceTypesResponse) -> dict:
    out: dict = {}
    if "target_resource_types" in value:
        import aws_sdk_fis.types.target_resource_type_summary_list

        out["targetResourceTypes"] = (
            aws_sdk_fis.types.target_resource_type_summary_list.serialize_json(
                value["target_resource_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTargetResourceTypesResponse:
    out: ListTargetResourceTypesResponse = {}  # type: ignore[typeddict-item]
    if "targetResourceTypes" in data:
        import aws_sdk_fis.types.target_resource_type_summary_list

        out["target_resource_types"] = (
            aws_sdk_fis.types.target_resource_type_summary_list.deserialize_json(
                data["targetResourceTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
