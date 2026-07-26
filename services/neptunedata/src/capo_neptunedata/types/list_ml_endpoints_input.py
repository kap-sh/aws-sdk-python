"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListMLEndpointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.positive_integer


class ListMLEndpointsInput(TypedDict, closed=True):
    max_items: NotRequired["capo_neptunedata.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of items to return (from 1 to 1024; the default is 10.</p>"""
    neptune_iam_role_arn: NotRequired["str"]
    """<p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMLEndpointsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMLEndpointsInput:
    out: ListMLEndpointsInput = {}  # type: ignore[typeddict-item]
    return out
