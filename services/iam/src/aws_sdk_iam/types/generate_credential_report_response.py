"""Generated from Smithy shape ``com.amazonaws.iam#GenerateCredentialReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.report_state_description_type
    import aws_sdk_iam.types.report_state_type


class GenerateCredentialReportResponse(TypedDict, closed=True):
    state: NotRequired["aws_sdk_iam.types.report_state_type.ReportStateType"]
    """<p>Information about the state of the credential report.</p>"""
    description: NotRequired[
        "aws_sdk_iam.types.report_state_description_type.ReportStateDescriptionType"
    ]
    """<p>Information about the credential report.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GenerateCredentialReportResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import aws_sdk_iam.types.report_state_type

        aws_sdk_iam.types.report_state_type.serialize_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_query(el: Element) -> GenerateCredentialReportResponse:
    out: GenerateCredentialReportResponse = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_iam.types.report_state_type

        out["state"] = aws_sdk_iam.types.report_state_type.deserialize_query(
            child_state
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
