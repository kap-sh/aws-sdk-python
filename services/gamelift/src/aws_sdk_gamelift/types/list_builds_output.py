"""Generated from Smithy shape ``com.amazonaws.gamelift#ListBuildsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build_list
    import aws_sdk_gamelift.types.non_empty_string


class ListBuildsOutput(TypedDict, closed=True):
    builds: NotRequired["aws_sdk_gamelift.types.build_list.BuildList"]
    """<p>A collection of build resources that match the request.</p>"""
    next_token: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildsOutput) -> dict:
    out: dict = {}
    if "builds" in value:
        import aws_sdk_gamelift.types.build_list

        out["Builds"] = aws_sdk_gamelift.types.build_list.serialize_aws_json_1_1(
            value["builds"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildsOutput:
    out: ListBuildsOutput = {}  # type: ignore[typeddict-item]
    if "Builds" in data:
        import aws_sdk_gamelift.types.build_list

        out["builds"] = aws_sdk_gamelift.types.build_list.deserialize_aws_json_1_1(
            data["Builds"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
