"""Generated from Smithy shape ``com.amazonaws.iam#GetHumanReadableSummaryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.locale_type
    import aws_sdk_iam.types.summary_content_type
    import aws_sdk_iam.types.summary_state_type


class GetHumanReadableSummaryResponse(TypedDict):
    summary_content: NotRequired[
        "aws_sdk_iam.types.summary_content_type.summaryContentType"
    ]
    """<p>Summary content in the specified locale. Summary content is non-empty only if the <code>SummaryState</code> is <code>AVAILABLE</code>.</p>"""
    locale: NotRequired["aws_sdk_iam.types.locale_type.localeType"]
    """<p>The locale that this response was generated for. This maps to the input locale.</p>"""
    summary_state: NotRequired["aws_sdk_iam.types.summary_state_type.summaryStateType"]
    """<p>State of summary generation. This generation process is asynchronous and this attribute indicates the state of the generation process.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetHumanReadableSummaryResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "summary_content" in value:
        pairs.append((f"{prefix}.SummaryContent", str(value["summary_content"])))
    if "locale" in value:
        pairs.append((f"{prefix}.Locale", str(value["locale"])))
    if "summary_state" in value:
        import aws_sdk_iam.types.summary_state_type

        aws_sdk_iam.types.summary_state_type.serialize_query(
            value["summary_state"], pairs, f"{prefix}.SummaryState"
        )


def deserialize_query(el: Element) -> GetHumanReadableSummaryResponse:
    out: GetHumanReadableSummaryResponse = {}  # type: ignore[typeddict-item]
    child_summary_content = el.find("SummaryContent")
    if child_summary_content is not None:
        out["summary_content"] = str(child_summary_content.text or "")
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_summary_state = el.find("SummaryState")
    if child_summary_state is not None:
        import aws_sdk_iam.types.summary_state_type

        out["summary_state"] = aws_sdk_iam.types.summary_state_type.deserialize_query(
            child_summary_state
        )
    return out
