"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteIdNamespaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name


class DeleteIdNamespaceInput(TypedDict, closed=True):
    id_namespace_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the ID namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdNamespaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIdNamespaceInput:
    out: DeleteIdNamespaceInput = {}  # type: ignore[typeddict-item]
    return out
