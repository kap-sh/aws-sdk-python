"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateTestSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name


class UpdateTestSetRequest(TypedDict, closed=True):
    test_set_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The test set Id for which update test operation to be performed.</p>"""
    test_set_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The new test set name.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The new test set description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTestSetRequest) -> dict:
    out: dict = {}
    out["testSetName"] = value["test_set_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateTestSetRequest:
    out: UpdateTestSetRequest = {}  # type: ignore[typeddict-item]
    if "testSetName" in data:
        out["test_set_name"] = data["testSetName"]
    else:
        raise DeserializationError("UpdateTestSetRequest.test_set_name required")
    if "description" in data:
        out["description"] = data["description"]
    return out
