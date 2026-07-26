"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteTestSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id


class DeleteTestSetRequest(TypedDict, closed=True):
    test_set_id: "capo_lex_models_v2.types.id.Id"
    """<p>The test set Id of the test set to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTestSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTestSetRequest:
    out: DeleteTestSetRequest = {}  # type: ignore[typeddict-item]
    return out
