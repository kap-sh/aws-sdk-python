"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.composition_relationship


class CompositionDetails(TypedDict, closed=True):
    composition_relationship: NotRequired[
        "aws_sdk_iotsitewise.types.composition_relationship.CompositionRelationship"
    ]
    """<p>An array detailing the composition relationship for this composite model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositionDetails) -> dict:
    out: dict = {}
    if "composition_relationship" in value:
        import aws_sdk_iotsitewise.types.composition_relationship

        out["compositionRelationship"] = (
            aws_sdk_iotsitewise.types.composition_relationship.serialize_json(
                value["composition_relationship"]
            )
        )
    return out


def deserialize_json(data: dict) -> CompositionDetails:
    out: CompositionDetails = {}  # type: ignore[typeddict-item]
    if "compositionRelationship" in data:
        import aws_sdk_iotsitewise.types.composition_relationship

        out["composition_relationship"] = (
            aws_sdk_iotsitewise.types.composition_relationship.deserialize_json(
                data["compositionRelationship"]
            )
        )
    return out
