"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentEstimateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.status_code
    import aws_sdk_customer_profiles.types.string1_to255


class CreateSegmentEstimateResponse(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The unique name of the domain.</p>"""
    estimate_id: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>A unique identifier for the resource. The value can be passed to <code>GetSegmentEstimate</code> to retrieve the result of segment estimate status.</p>"""
    status_code: "aws_sdk_customer_profiles.types.status_code.StatusCode"
    """<p>The status code for the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentEstimateResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "estimate_id" in value:
        out["EstimateId"] = value["estimate_id"]
    return out


def deserialize_json(data: dict) -> CreateSegmentEstimateResponse:
    out: CreateSegmentEstimateResponse = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "EstimateId" in data:
        out["estimate_id"] = data["EstimateId"]
    return out
