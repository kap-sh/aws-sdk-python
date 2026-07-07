"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListActionTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_owner
    import aws_sdk_codepipeline.types.aws_region_name
    import aws_sdk_codepipeline.types.next_token


class ListActionTypesInput(TypedDict, closed=True):
    action_owner_filter: NotRequired[
        "aws_sdk_codepipeline.types.action_owner.ActionOwner"
    ]
    """<p>Filters the list of action types to those created by a specified entity.</p>"""
    next_token: NotRequired["aws_sdk_codepipeline.types.next_token.NextToken"]
    """<p>An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.</p>"""
    region_filter: NotRequired[
        "aws_sdk_codepipeline.types.aws_region_name.AWSRegionName"
    ]
    """<p>The Region to filter on for the list of action types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActionTypesInput) -> dict:
    out: dict = {}
    if "action_owner_filter" in value:
        import aws_sdk_codepipeline.types.action_owner

        out["actionOwnerFilter"] = (
            aws_sdk_codepipeline.types.action_owner.serialize_aws_json_1_1(
                value["action_owner_filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "region_filter" in value:
        out["regionFilter"] = value["region_filter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActionTypesInput:
    out: ListActionTypesInput = {}  # type: ignore[typeddict-item]
    if "actionOwnerFilter" in data:
        import aws_sdk_codepipeline.types.action_owner

        out["action_owner_filter"] = (
            aws_sdk_codepipeline.types.action_owner.deserialize_aws_json_1_1(
                data["actionOwnerFilter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "regionFilter" in data:
        out["region_filter"] = data["regionFilter"]
    return out
