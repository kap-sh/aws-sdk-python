"""Generated from Smithy shape ``com.amazonaws.inspector2#TitleAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.severity_counts


class TitleAggregationResponse(TypedDict, closed=True):
    title: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The title that the findings were aggregated on.</p>"""
    vulnerability_id: NotRequired["str"]
    """<p>The vulnerability ID of the finding.</p>"""
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account associated with the findings.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_inspector2.types.severity_counts.SeverityCounts"
    ]
    """<p>An object that represent the count of matched findings per severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TitleAggregationResponse) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    if "vulnerability_id" in value:
        out["vulnerabilityId"] = value["vulnerability_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import aws_sdk_inspector2.types.severity_counts

        out["severityCounts"] = aws_sdk_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> TitleAggregationResponse:
    out: TitleAggregationResponse = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("TitleAggregationResponse.title required")
    if "vulnerabilityId" in data:
        out["vulnerability_id"] = data["vulnerabilityId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severityCounts" in data:
        import aws_sdk_inspector2.types.severity_counts

        out["severity_counts"] = (
            aws_sdk_inspector2.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    return out
