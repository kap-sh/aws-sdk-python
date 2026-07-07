"""Generated from Smithy shape ``com.amazonaws.inspector2#PackageAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.severity_counts


class PackageAggregationResponse(TypedDict, closed=True):
    package_name: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The name of the operating system package.</p>"""
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account associated with the findings.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_inspector2.types.severity_counts.SeverityCounts"
    ]
    """<p>An object that contains the count of matched findings per severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageAggregationResponse) -> dict:
    out: dict = {}
    out["packageName"] = value["package_name"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import aws_sdk_inspector2.types.severity_counts

        out["severityCounts"] = aws_sdk_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> PackageAggregationResponse:
    out: PackageAggregationResponse = {}  # type: ignore[typeddict-item]
    if "packageName" in data:
        out["package_name"] = data["packageName"]
    else:
        raise DeserializationError("PackageAggregationResponse.package_name required")
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
