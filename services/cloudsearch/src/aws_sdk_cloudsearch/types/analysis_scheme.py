"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AnalysisScheme``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.analysis_options
    import aws_sdk_cloudsearch.types.analysis_scheme_language
    import aws_sdk_cloudsearch.types.standard_name


class AnalysisScheme(TypedDict):
    analysis_scheme_name: "aws_sdk_cloudsearch.types.standard_name.StandardName"
    analysis_scheme_language: (
        "aws_sdk_cloudsearch.types.analysis_scheme_language.AnalysisSchemeLanguage"
    )
    analysis_options: NotRequired[
        "aws_sdk_cloudsearch.types.analysis_options.AnalysisOptions"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AnalysisScheme, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.AnalysisSchemeName", str(value["analysis_scheme_name"])))
    import aws_sdk_cloudsearch.types.analysis_scheme_language

    aws_sdk_cloudsearch.types.analysis_scheme_language.serialize_query(
        value["analysis_scheme_language"], pairs, f"{prefix}.AnalysisSchemeLanguage"
    )
    if "analysis_options" in value:
        import aws_sdk_cloudsearch.types.analysis_options

        aws_sdk_cloudsearch.types.analysis_options.serialize_query(
            value["analysis_options"], pairs, f"{prefix}.AnalysisOptions"
        )


def deserialize_query(el: Element) -> AnalysisScheme:
    out: AnalysisScheme = {}  # type: ignore[typeddict-item]
    child_analysis_scheme_name = el.find("AnalysisSchemeName")
    if child_analysis_scheme_name is not None:
        out["analysis_scheme_name"] = str(child_analysis_scheme_name.text or "")
    else:
        raise DeserializationError("AnalysisScheme.analysis_scheme_name required")
    child_analysis_scheme_language = el.find("AnalysisSchemeLanguage")
    if child_analysis_scheme_language is not None:
        import aws_sdk_cloudsearch.types.analysis_scheme_language

        out["analysis_scheme_language"] = (
            aws_sdk_cloudsearch.types.analysis_scheme_language.deserialize_query(
                child_analysis_scheme_language
            )
        )
    else:
        raise DeserializationError("AnalysisScheme.analysis_scheme_language required")
    child_analysis_options = el.find("AnalysisOptions")
    if child_analysis_options is not None:
        import aws_sdk_cloudsearch.types.analysis_options

        out["analysis_options"] = (
            aws_sdk_cloudsearch.types.analysis_options.deserialize_query(
                child_analysis_options
            )
        )
    return out
