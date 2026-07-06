"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StartRecommendationReportGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.group_ids
    import aws_sdk_migrationhubstrategy.types.output_format


class StartRecommendationReportGenerationRequest(TypedDict, closed=True):
    output_format: NotRequired[
        "aws_sdk_migrationhubstrategy.types.output_format.OutputFormat"
    ]
    """<p> The output format for the recommendation report file. The default format is Microsoft Excel. </p>"""
    group_id_filter: NotRequired[
        "aws_sdk_migrationhubstrategy.types.group_ids.GroupIds"
    ]
    """<p> Groups the resources in the recommendation report with a unique name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecommendationReportGenerationRequest) -> dict:
    out: dict = {}
    if "output_format" in value:
        out["outputFormat"] = value["output_format"]
    if "group_id_filter" in value:
        import aws_sdk_migrationhubstrategy.types.group_ids

        out["groupIdFilter"] = (
            aws_sdk_migrationhubstrategy.types.group_ids.serialize_json(
                value["group_id_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartRecommendationReportGenerationRequest:
    out: StartRecommendationReportGenerationRequest = {}  # type: ignore[typeddict-item]
    if "outputFormat" in data:
        out["output_format"] = data["outputFormat"]
    if "groupIdFilter" in data:
        import aws_sdk_migrationhubstrategy.types.group_ids

        out["group_id_filter"] = (
            aws_sdk_migrationhubstrategy.types.group_ids.deserialize_json(
                data["groupIdFilter"]
            )
        )
    return out
