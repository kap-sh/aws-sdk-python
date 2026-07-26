"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineAnalysisSchemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.analysis_scheme_status


class DefineAnalysisSchemeResponse(TypedDict, closed=True):
    analysis_scheme: (
        "capo_cloudsearch.types.analysis_scheme_status.AnalysisSchemeStatus"
    )


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineAnalysisSchemeResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.analysis_scheme_status

    capo_cloudsearch.types.analysis_scheme_status.serialize_query(
        value["analysis_scheme"], pairs, f"{prefix}.AnalysisScheme"
    )


def deserialize_query(el: Element) -> DefineAnalysisSchemeResponse:
    out: DefineAnalysisSchemeResponse = {}  # type: ignore[typeddict-item]
    child_analysis_scheme = el.find("AnalysisScheme")
    if child_analysis_scheme is not None:
        import capo_cloudsearch.types.analysis_scheme_status

        out["analysis_scheme"] = (
            capo_cloudsearch.types.analysis_scheme_status.deserialize_query(
                child_analysis_scheme
            )
        )
    else:
        raise DeserializationError(
            "DefineAnalysisSchemeResponse.analysis_scheme required"
        )
    return out
