"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.kpi_field_wells
    import aws_sdk_quicksight.types.kpi_options
    import aws_sdk_quicksight.types.kpi_sort_configuration
    import aws_sdk_quicksight.types.visual_interaction_options


class KPIConfiguration(TypedDict, closed=True):
    field_wells: NotRequired["aws_sdk_quicksight.types.kpi_field_wells.KPIFieldWells"]
    """<p>The field well configuration of a KPI visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.kpi_sort_configuration.KPISortConfiguration"
    ]
    """<p>The sort configuration of a KPI visual.</p>"""
    kpi_options: NotRequired["aws_sdk_quicksight.types.kpi_options.KPIOptions"]
    """<p>The options that determine the presentation of a KPI visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.kpi_field_wells

        out["FieldWells"] = aws_sdk_quicksight.types.kpi_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.kpi_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.kpi_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "kpi_options" in value:
        import aws_sdk_quicksight.types.kpi_options

        out["KPIOptions"] = aws_sdk_quicksight.types.kpi_options.serialize_json(
            value["kpi_options"]
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIConfiguration:
    out: KPIConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.kpi_field_wells

        out["field_wells"] = aws_sdk_quicksight.types.kpi_field_wells.deserialize_json(
            data["FieldWells"]
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.kpi_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.kpi_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "KPIOptions" in data:
        import aws_sdk_quicksight.types.kpi_options

        out["kpi_options"] = aws_sdk_quicksight.types.kpi_options.deserialize_json(
            data["KPIOptions"]
        )
    if "Interactions" in data:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
