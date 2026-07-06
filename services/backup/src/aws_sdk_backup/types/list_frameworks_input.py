"""Generated from Smithy shape ``com.amazonaws.backup#ListFrameworksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.max_framework_inputs
    import aws_sdk_backup.types.string


class ListFrameworksInput(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_backup.types.max_framework_inputs.MaxFrameworkInputs"
    ]
    """<p>The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFrameworksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFrameworksInput:
    out: ListFrameworksInput = {}  # type: ignore[typeddict-item]
    return out
