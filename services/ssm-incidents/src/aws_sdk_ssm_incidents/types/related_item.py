"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RelatedItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.generated_id
    import aws_sdk_ssm_incidents.types.item_identifier


class RelatedItem(TypedDict, closed=True):
    identifier: "aws_sdk_ssm_incidents.types.item_identifier.ItemIdentifier"
    """<p>Details about the related item.</p>"""
    title: NotRequired["str"]
    """<p>The title of the related item.</p>"""
    generated_id: NotRequired["aws_sdk_ssm_incidents.types.generated_id.GeneratedId"]
    """<p>A unique ID for a <code>RelatedItem</code>.</p> <important> <p>Don't specify this parameter when you add a <code>RelatedItem</code> by using the <a>UpdateRelatedItems</a> API action.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItem) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.item_identifier

    out["identifier"] = aws_sdk_ssm_incidents.types.item_identifier.serialize_json(
        value["identifier"]
    )
    if "title" in value:
        out["title"] = value["title"]
    if "generated_id" in value:
        out["generatedId"] = value["generated_id"]
    return out


def deserialize_json(data: dict) -> RelatedItem:
    out: RelatedItem = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        import aws_sdk_ssm_incidents.types.item_identifier

        out["identifier"] = (
            aws_sdk_ssm_incidents.types.item_identifier.deserialize_json(
                data["identifier"]
            )
        )
    else:
        raise DeserializationError("RelatedItem.identifier required")
    if "title" in data:
        out["title"] = data["title"]
    if "generatedId" in data:
        out["generated_id"] = data["generatedId"]
    return out
