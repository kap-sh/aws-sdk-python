"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.summary_map_type


class GetAccountSummaryResponse(TypedDict, closed=True):
    summary_map: NotRequired["capo_iam.types.summary_map_type.summaryMapType"]
    """<p>A set of key–value pairs containing information about IAM entity usage and IAM quotas.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccountSummaryResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "summary_map" in value:
        import capo_iam.types.summary_map_type

        capo_iam.types.summary_map_type.serialize_query(
            value["summary_map"], pairs, f"{key_prefix}SummaryMap"
        )


def deserialize_query(el: Element) -> GetAccountSummaryResponse:
    out: GetAccountSummaryResponse = {}  # type: ignore[typeddict-item]
    child_summary_map = el.find("SummaryMap")
    if child_summary_map is not None:
        import capo_iam.types.summary_map_type

        out["summary_map"] = capo_iam.types.summary_map_type.deserialize_query(
            child_summary_map
        )
    return out
