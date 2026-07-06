"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeAnalysisSchemesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.analysis_scheme_status_list


class DescribeAnalysisSchemesResponse(TypedDict, closed=True):
    analysis_schemes: (
        "aws_sdk_cloudsearch.types.analysis_scheme_status_list.AnalysisSchemeStatusList"
    )
    """<p>The analysis scheme descriptions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAnalysisSchemesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.analysis_scheme_status_list

    aws_sdk_cloudsearch.types.analysis_scheme_status_list.serialize_query(
        value["analysis_schemes"], pairs, f"{prefix}.AnalysisSchemes"
    )


def deserialize_query(el: Element) -> DescribeAnalysisSchemesResponse:
    out: DescribeAnalysisSchemesResponse = {}  # type: ignore[typeddict-item]
    child_analysis_schemes = el.find("AnalysisSchemes")
    if child_analysis_schemes is not None:
        import aws_sdk_cloudsearch.types.analysis_scheme_status_list

        out["analysis_schemes"] = (
            aws_sdk_cloudsearch.types.analysis_scheme_status_list.deserialize_query(
                child_analysis_schemes
            )
        )
    else:
        raise DeserializationError(
            "DescribeAnalysisSchemesResponse.analysis_schemes required"
        )
    return out
