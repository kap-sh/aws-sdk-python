"""Generated from Smithy shape ``com.amazonaws.odb#ListDbSystemShapesInput``."""

from typing_extensions import NotRequired, TypedDict


class ListDbSystemShapesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The logical name of the AZ, for example, us-east-1a. This name varies depending on the account.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The physical ID of the AZ, for example, use1-az4. This ID persists across accounts.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbSystemShapesInput) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbSystemShapesInput:
    out: ListDbSystemShapesInput = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    return out
