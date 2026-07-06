"""Generated from Smithy shape ``com.amazonaws.fis#ListExperimentResolvedTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.next_token
    import aws_sdk_fis.types.resolved_target_list


class ListExperimentResolvedTargetsResponse(TypedDict, closed=True):
    resolved_targets: NotRequired[
        "aws_sdk_fis.types.resolved_target_list.ResolvedTargetList"
    ]
    """<p>The resolved targets.</p>"""
    next_token: NotRequired["aws_sdk_fis.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentResolvedTargetsResponse) -> dict:
    out: dict = {}
    if "resolved_targets" in value:
        import aws_sdk_fis.types.resolved_target_list

        out["resolvedTargets"] = aws_sdk_fis.types.resolved_target_list.serialize_json(
            value["resolved_targets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExperimentResolvedTargetsResponse:
    out: ListExperimentResolvedTargetsResponse = {}  # type: ignore[typeddict-item]
    if "resolvedTargets" in data:
        import aws_sdk_fis.types.resolved_target_list

        out["resolved_targets"] = (
            aws_sdk_fis.types.resolved_target_list.deserialize_json(
                data["resolvedTargets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
