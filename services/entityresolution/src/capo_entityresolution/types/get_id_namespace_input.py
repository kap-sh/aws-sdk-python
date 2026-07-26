"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetIdNamespaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name_or_id_namespace_arn


class GetIdNamespaceInput(TypedDict, closed=True):
    id_namespace_name: "capo_entityresolution.types.entity_name_or_id_namespace_arn.EntityNameOrIdNamespaceArn"
    """<p>The name of the ID namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdNamespaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdNamespaceInput:
    out: GetIdNamespaceInput = {}  # type: ignore[typeddict-item]
    return out
