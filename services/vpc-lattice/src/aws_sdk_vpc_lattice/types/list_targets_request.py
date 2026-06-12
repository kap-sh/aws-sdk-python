"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListTargetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.target_group_identifier
    import aws_sdk_vpc_lattice.types.target_list


class ListTargetsRequest(TypedDict):
    target_group_identifier: (
        "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier"
    )
    """<p>The ID or ARN of the target group.</p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""
    targets: NotRequired["aws_sdk_vpc_lattice.types.target_list.TargetList"]
    """<p>The targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsRequest) -> dict:
    out: dict = {}
    if "targets" in value:
        import aws_sdk_vpc_lattice.types.target_list

        out["targets"] = aws_sdk_vpc_lattice.types.target_list.serialize_json(
            value["targets"]
        )
    return out


def deserialize_json(data: dict) -> ListTargetsRequest:
    out: ListTargetsRequest = {}  # type: ignore[typeddict-item]
    if "targets" in data:
        import aws_sdk_vpc_lattice.types.target_list

        out["targets"] = aws_sdk_vpc_lattice.types.target_list.deserialize_json(
            data["targets"]
        )
    return out
