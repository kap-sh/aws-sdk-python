"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AnalysisSchemeStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.analysis_scheme
    import aws_sdk_cloudsearch.types.option_status


class AnalysisSchemeStatus(TypedDict, closed=True):
    options: "aws_sdk_cloudsearch.types.analysis_scheme.AnalysisScheme"
    status: "aws_sdk_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: AnalysisSchemeStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.analysis_scheme

    aws_sdk_cloudsearch.types.analysis_scheme.serialize_query(
        value["options"], pairs, f"{prefix}.Options"
    )
    import aws_sdk_cloudsearch.types.option_status

    aws_sdk_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> AnalysisSchemeStatus:
    out: AnalysisSchemeStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_cloudsearch.types.analysis_scheme

        out["options"] = aws_sdk_cloudsearch.types.analysis_scheme.deserialize_query(
            child_options
        )
    else:
        raise DeserializationError("AnalysisSchemeStatus.options required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudsearch.types.option_status

        out["status"] = aws_sdk_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("AnalysisSchemeStatus.status required")
    return out
