"""Generated from Smithy shape ``com.amazonaws.oam#ListAttachedLinksItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_oam.types.resource_types_output


class ListAttachedLinksItem(TypedDict):
    label: NotRequired["str"]
    """<p>The label that was assigned to this link at creation, with the variables resolved to their actual values.</p>"""
    link_arn: NotRequired["str"]
    """<p>The ARN of the link.</p>"""
    resource_types: NotRequired[
        "aws_sdk_oam.types.resource_types_output.ResourceTypesOutput"
    ]
    """<p>The resource types supported by this link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedLinksItem) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    if "link_arn" in value:
        out["LinkArn"] = value["link_arn"]
    if "resource_types" in value:
        import aws_sdk_oam.types.resource_types_output

        out["ResourceTypes"] = aws_sdk_oam.types.resource_types_output.serialize_json(
            value["resource_types"]
        )
    return out


def deserialize_json(data: dict) -> ListAttachedLinksItem:
    out: ListAttachedLinksItem = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        out["label"] = data["Label"]
    if "LinkArn" in data:
        out["link_arn"] = data["LinkArn"]
    if "ResourceTypes" in data:
        import aws_sdk_oam.types.resource_types_output

        out["resource_types"] = (
            aws_sdk_oam.types.resource_types_output.deserialize_json(
                data["ResourceTypes"]
            )
        )
    return out
