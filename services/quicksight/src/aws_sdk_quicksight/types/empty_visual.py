"""Generated from Smithy shape ``com.amazonaws.quicksight#EmptyVisual``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_identifier
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.visual_custom_action_list


class EmptyVisual(TypedDict, closed=True):
    visual_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.</p>"""
    data_set_identifier: (
        "aws_sdk_quicksight.types.data_set_identifier.DataSetIdentifier"
    )
    """<p>The data set that is used in the empty visual. Every visual requires a dataset to render.</p>"""
    actions: NotRequired[
        "aws_sdk_quicksight.types.visual_custom_action_list.VisualCustomActionList"
    ]
    """<p>The list of custom actions that are configured for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmptyVisual) -> dict:
    out: dict = {}
    out["VisualId"] = value["visual_id"]
    out["DataSetIdentifier"] = value["data_set_identifier"]
    if "actions" in value:
        import aws_sdk_quicksight.types.visual_custom_action_list

        out["Actions"] = (
            aws_sdk_quicksight.types.visual_custom_action_list.serialize_json(
                value["actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmptyVisual:
    out: EmptyVisual = {}  # type: ignore[typeddict-item]
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("EmptyVisual.visual_id required")
    if "DataSetIdentifier" in data:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        raise DeserializationError("EmptyVisual.data_set_identifier required")
    if "Actions" in data:
        import aws_sdk_quicksight.types.visual_custom_action_list

        out["actions"] = (
            aws_sdk_quicksight.types.visual_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    return out
