"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditSuppressionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ascending_order
    import aws_sdk_iot.types.audit_check_name
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.resource_identifier


class ListAuditSuppressionsRequest(TypedDict):
    check_name: NotRequired["aws_sdk_iot.types.audit_check_name.AuditCheckName"]
    resource_identifier: NotRequired[
        "aws_sdk_iot.types.resource_identifier.ResourceIdentifier"
    ]
    ascending_order: "aws_sdk_iot.types.ascending_order.AscendingOrder"
    """<p> Determines whether suppressions are listed in ascending order by expiration date or not. If parameter isn't provided, <code>ascendingOrder=true</code>. </p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> The token for the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p> The maximum number of results to return at one time. The default is 25. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditSuppressionsRequest) -> dict:
    out: dict = {}
    if "check_name" in value:
        out["checkName"] = value["check_name"]
    if "resource_identifier" in value:
        import aws_sdk_iot.types.resource_identifier

        out["resourceIdentifier"] = (
            aws_sdk_iot.types.resource_identifier.serialize_json(
                value["resource_identifier"]
            )
        )
    out["ascendingOrder"] = value.get("ascending_order", False)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAuditSuppressionsRequest:
    out: ListAuditSuppressionsRequest = {}  # type: ignore[typeddict-item]
    if "checkName" in data:
        out["check_name"] = data["checkName"]
    if "resourceIdentifier" in data:
        import aws_sdk_iot.types.resource_identifier

        out["resource_identifier"] = (
            aws_sdk_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    if "ascendingOrder" in data:
        out["ascending_order"] = data["ascendingOrder"]
    else:
        out["ascending_order"] = False
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
