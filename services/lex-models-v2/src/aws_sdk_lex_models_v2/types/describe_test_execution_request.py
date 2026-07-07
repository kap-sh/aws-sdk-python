"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeTestExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class DescribeTestExecutionRequest(TypedDict, closed=True):
    test_execution_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The execution Id of the test set execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTestExecutionRequest:
    out: DescribeTestExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
