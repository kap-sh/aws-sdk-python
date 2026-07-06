"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteAnalysisSchemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.analysis_scheme_status


class DeleteAnalysisSchemeResponse(TypedDict, closed=True):
    analysis_scheme: (
        "aws_sdk_cloudsearch.types.analysis_scheme_status.AnalysisSchemeStatus"
    )
    """<p>The status of the analysis scheme being deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAnalysisSchemeResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.analysis_scheme_status

    aws_sdk_cloudsearch.types.analysis_scheme_status.serialize_query(
        value["analysis_scheme"], pairs, f"{prefix}.AnalysisScheme"
    )


def deserialize_query(el: Element) -> DeleteAnalysisSchemeResponse:
    out: DeleteAnalysisSchemeResponse = {}  # type: ignore[typeddict-item]
    child_analysis_scheme = el.find("AnalysisScheme")
    if child_analysis_scheme is not None:
        import aws_sdk_cloudsearch.types.analysis_scheme_status

        out["analysis_scheme"] = (
            aws_sdk_cloudsearch.types.analysis_scheme_status.deserialize_query(
                child_analysis_scheme
            )
        )
    else:
        raise DeserializationError(
            "DeleteAnalysisSchemeResponse.analysis_scheme required"
        )
    return out
