"""Generated from Smithy shape ``com.amazonaws.lambda#Filter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.pattern


class Filter(TypedDict):
    pattern: NotRequired["aws_sdk_lambda.types.pattern.Pattern"]
    """<p> A filter pattern. For more information on the syntax of a filter pattern, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax\"> Filter rule syntax</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Pattern" in data:
        out["pattern"] = data["Pattern"]
    return out
