"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineAnalysisSchemeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.analysis_scheme
    import aws_sdk_cloudsearch.types.domain_name


class DefineAnalysisSchemeRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    analysis_scheme: "aws_sdk_cloudsearch.types.analysis_scheme.AnalysisScheme"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineAnalysisSchemeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    import aws_sdk_cloudsearch.types.analysis_scheme

    aws_sdk_cloudsearch.types.analysis_scheme.serialize_query(
        value["analysis_scheme"], pairs, f"{prefix}.AnalysisScheme"
    )


def deserialize_query(el: Element) -> DefineAnalysisSchemeRequest:
    out: DefineAnalysisSchemeRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DefineAnalysisSchemeRequest.domain_name required")
    child_analysis_scheme = el.find("AnalysisScheme")
    if child_analysis_scheme is not None:
        import aws_sdk_cloudsearch.types.analysis_scheme

        out["analysis_scheme"] = (
            aws_sdk_cloudsearch.types.analysis_scheme.deserialize_query(
                child_analysis_scheme
            )
        )
    else:
        raise DeserializationError(
            "DefineAnalysisSchemeRequest.analysis_scheme required"
        )
    return out
