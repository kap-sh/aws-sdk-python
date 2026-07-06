"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListLensSharesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.list_workload_shares_max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.share_status
    import aws_sdk_wellarchitected.types.shared_with_prefix


class ListLensSharesInput(TypedDict, closed=True):
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    shared_with_prefix: NotRequired[
        "aws_sdk_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
    ]
    """<p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the lens is shared.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "aws_sdk_wellarchitected.types.list_workload_shares_max_results.ListWorkloadSharesMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    status: NotRequired["aws_sdk_wellarchitected.types.share_status.ShareStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLensSharesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLensSharesInput:
    out: ListLensSharesInput = {}  # type: ignore[typeddict-item]
    return out
