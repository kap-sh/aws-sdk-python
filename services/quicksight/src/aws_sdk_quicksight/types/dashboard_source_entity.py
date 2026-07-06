"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardSourceEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_source_template


class DashboardSourceEntity(TypedDict, closed=True):
    source_template: NotRequired[
        "aws_sdk_quicksight.types.dashboard_source_template.DashboardSourceTemplate"
    ]
    """<p>Source template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardSourceEntity) -> dict:
    out: dict = {}
    if "source_template" in value:
        import aws_sdk_quicksight.types.dashboard_source_template

        out["SourceTemplate"] = (
            aws_sdk_quicksight.types.dashboard_source_template.serialize_json(
                value["source_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashboardSourceEntity:
    out: DashboardSourceEntity = {}  # type: ignore[typeddict-item]
    if "SourceTemplate" in data:
        import aws_sdk_quicksight.types.dashboard_source_template

        out["source_template"] = (
            aws_sdk_quicksight.types.dashboard_source_template.deserialize_json(
                data["SourceTemplate"]
            )
        )
    return out
