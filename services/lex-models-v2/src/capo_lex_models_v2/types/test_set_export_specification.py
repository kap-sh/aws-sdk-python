"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetExportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id


class TestSetExportSpecification(TypedDict, closed=True):
    test_set_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the test set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetExportSpecification) -> dict:
    out: dict = {}
    out["testSetId"] = value["test_set_id"]
    return out


def deserialize_json(data: dict) -> TestSetExportSpecification:
    out: TestSetExportSpecification = {}  # type: ignore[typeddict-item]
    if "testSetId" in data:
        out["test_set_id"] = data["testSetId"]
    else:
        raise DeserializationError("TestSetExportSpecification.test_set_id required")
    return out
