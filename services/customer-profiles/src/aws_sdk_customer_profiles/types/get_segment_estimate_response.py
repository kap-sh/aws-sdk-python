"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentEstimateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.estimate_status
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.status_code
    import aws_sdk_customer_profiles.types.string1_to255


class GetSegmentEstimateResponse(TypedDict):
    domain_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The unique name of the domain.</p>"""
    estimate_id: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The <code>QueryId</code> which is the same as the value passed in <code>QueryId</code>.</p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.estimate_status.EstimateStatus"
    ]
    """<p>The current status of the query.</p>"""
    estimate: NotRequired["aws_sdk_customer_profiles.types.string1_to255.string1To255"]
    """<p>The estimated number of profiles contained in the segment.</p>"""
    message: NotRequired["aws_sdk_customer_profiles.types.string1_to255.string1To255"]
    """<p>The error message if there is any error.</p>"""
    status_code: "aws_sdk_customer_profiles.types.status_code.StatusCode"
    """<p>The status code of the segment estimate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentEstimateResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "estimate_id" in value:
        out["EstimateId"] = value["estimate_id"]
    if "status" in value:
        import aws_sdk_customer_profiles.types.estimate_status

        out["Status"] = aws_sdk_customer_profiles.types.estimate_status.serialize_json(
            value["status"]
        )
    if "estimate" in value:
        out["Estimate"] = value["estimate"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetSegmentEstimateResponse:
    out: GetSegmentEstimateResponse = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "EstimateId" in data:
        out["estimate_id"] = data["EstimateId"]
    if "Status" in data:
        import aws_sdk_customer_profiles.types.estimate_status

        out["status"] = (
            aws_sdk_customer_profiles.types.estimate_status.deserialize_json(
                data["Status"]
            )
        )
    if "Estimate" in data:
        out["estimate"] = data["Estimate"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
