"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListRotationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.max_results
    import aws_sdk_ssm_contacts.types.pagination_token
    import aws_sdk_ssm_contacts.types.rotation_name


class ListRotationsRequest(TypedDict):
    rotation_name_prefix: NotRequired[
        "aws_sdk_ssm_contacts.types.rotation_name.RotationName"
    ]
    """<p>A filter to include rotations in list results based on their common prefix. For example, entering prod returns a list of all rotation names that begin with <code>prod</code>, such as <code>production</code> and <code>prod-1</code>.</p>"""
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRotationsRequest) -> dict:
    out: dict = {}
    if "rotation_name_prefix" in value:
        out["RotationNamePrefix"] = value["rotation_name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRotationsRequest:
    out: ListRotationsRequest = {}  # type: ignore[typeddict-item]
    if "RotationNamePrefix" in data:
        out["rotation_name_prefix"] = data["RotationNamePrefix"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
