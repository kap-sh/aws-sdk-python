"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Branch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.message
    import capo_iotfleetwise.types.string


class Branch(TypedDict, closed=True):
    fully_qualified_name: "capo_iotfleetwise.types.string.string"
    """<p>The fully qualified name of the branch. For example, the fully qualified name of a branch might be <code>Vehicle.Body.Engine</code>.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the branch.</p>"""
    deprecation_message: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>The deprecation message for the node or the branch that was moved or deleted.</p>"""
    comment: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>A comment in addition to the description.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Branch) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "deprecation_message" in value:
        out["deprecationMessage"] = value["deprecation_message"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Branch:
    out: Branch = {}  # type: ignore[typeddict-item]
    if "fullyQualifiedName" in data:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        raise DeserializationError("Branch.fully_qualified_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "deprecationMessage" in data:
        out["deprecation_message"] = data["deprecationMessage"]
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
