"""Generated from Smithy shape ``com.amazonaws.codebuild#ListFleetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_arns
    import aws_sdk_codebuild.types.string


class ListFleetsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""
    fleets: NotRequired["aws_sdk_codebuild.types.fleet_arns.FleetArns"]
    """<p>The list of compute fleet names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFleetsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "fleets" in value:
        import aws_sdk_codebuild.types.fleet_arns

        out["fleets"] = aws_sdk_codebuild.types.fleet_arns.serialize_aws_json_1_1(
            value["fleets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFleetsOutput:
    out: ListFleetsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "fleets" in data:
        import aws_sdk_codebuild.types.fleet_arns

        out["fleets"] = aws_sdk_codebuild.types.fleet_arns.deserialize_aws_json_1_1(
            data["fleets"]
        )
    return out
