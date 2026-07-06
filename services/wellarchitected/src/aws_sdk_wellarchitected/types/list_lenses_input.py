"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListLensesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_name
    import aws_sdk_wellarchitected.types.lens_status_type
    import aws_sdk_wellarchitected.types.lens_type
    import aws_sdk_wellarchitected.types.max_results
    import aws_sdk_wellarchitected.types.next_token


class ListLensesInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["aws_sdk_wellarchitected.types.max_results.MaxResults"]
    lens_type: NotRequired["aws_sdk_wellarchitected.types.lens_type.LensType"]
    """<p>The type of lenses to be returned.</p>"""
    lens_status: NotRequired[
        "aws_sdk_wellarchitected.types.lens_status_type.LensStatusType"
    ]
    """<p>The status of lenses to be returned.</p>"""
    lens_name: NotRequired["aws_sdk_wellarchitected.types.lens_name.LensName"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLensesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLensesInput:
    out: ListLensesInput = {}  # type: ignore[typeddict-item]
    return out
