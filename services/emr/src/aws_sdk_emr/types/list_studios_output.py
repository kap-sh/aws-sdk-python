"""Generated from Smithy shape ``com.amazonaws.emr#ListStudiosOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.marker
    import aws_sdk_emr.types.studio_summary_list


class ListStudiosOutput(TypedDict, closed=True):
    studios: NotRequired["aws_sdk_emr.types.studio_summary_list.StudioSummaryList"]
    """<p>The list of Studio summary objects.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStudiosOutput) -> dict:
    out: dict = {}
    if "studios" in value:
        import aws_sdk_emr.types.studio_summary_list

        out["Studios"] = aws_sdk_emr.types.studio_summary_list.serialize_aws_json_1_1(
            value["studios"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStudiosOutput:
    out: ListStudiosOutput = {}  # type: ignore[typeddict-item]
    if "Studios" in data:
        import aws_sdk_emr.types.studio_summary_list

        out["studios"] = aws_sdk_emr.types.studio_summary_list.deserialize_aws_json_1_1(
            data["Studios"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
