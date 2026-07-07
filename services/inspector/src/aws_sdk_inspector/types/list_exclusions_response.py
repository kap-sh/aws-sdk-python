"""Generated from Smithy shape ``com.amazonaws.inspector#ListExclusionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.list_returned_arn_list
    import aws_sdk_inspector.types.pagination_token


class ListExclusionsResponse(TypedDict, closed=True):
    exclusion_arns: "aws_sdk_inspector.types.list_returned_arn_list.ListReturnedArnList"
    """<p>A list of exclusions' ARNs returned by the action.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p>When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExclusionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.list_returned_arn_list

    out["exclusionArns"] = (
        aws_sdk_inspector.types.list_returned_arn_list.serialize_aws_json_1_1(
            value["exclusion_arns"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExclusionsResponse:
    out: ListExclusionsResponse = {}  # type: ignore[typeddict-item]
    if "exclusionArns" in data:
        import aws_sdk_inspector.types.list_returned_arn_list

        out["exclusion_arns"] = (
            aws_sdk_inspector.types.list_returned_arn_list.deserialize_aws_json_1_1(
                data["exclusionArns"]
            )
        )
    else:
        raise DeserializationError("ListExclusionsResponse.exclusion_arns required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
