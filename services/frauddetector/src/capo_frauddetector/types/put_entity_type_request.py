"""Generated from Smithy shape ``com.amazonaws.frauddetector#PutEntityTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.tag_list


class PutEntityTypeRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name of the entity type.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The description.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEntityTypeRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEntityTypeRequest:
    out: PutEntityTypeRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutEntityTypeRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
