"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeTestSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class DescribeTestSetRequest(TypedDict):
    test_set_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The test set Id for the test set request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTestSetRequest:
    out: DescribeTestSetRequest = {}  # type: ignore[typeddict-item]
    return out
