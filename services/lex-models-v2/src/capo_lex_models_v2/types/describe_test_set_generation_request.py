"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeTestSetGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id


class DescribeTestSetGenerationRequest(TypedDict, closed=True):
    test_set_generation_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the test set generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestSetGenerationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTestSetGenerationRequest:
    out: DescribeTestSetGenerationRequest = {}  # type: ignore[typeddict-item]
    return out
