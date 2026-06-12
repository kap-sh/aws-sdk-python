"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingSourceDetail``."""

from typing import TypedDict

from typing_extensions import NotRequired


class FindingSourceDetail(TypedDict):
    access_point_arn: NotRequired["str"]
    """<p>The ARN of the access point that generated the finding. The ARN format depends on whether the ARN represents an access point or a multi-region access point.</p>"""
    access_point_account: NotRequired["str"]
    """<p>The account of the cross-account access point that generated the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSourceDetail) -> dict:
    out: dict = {}
    if "access_point_arn" in value:
        out["accessPointArn"] = value["access_point_arn"]
    if "access_point_account" in value:
        out["accessPointAccount"] = value["access_point_account"]
    return out


def deserialize_json(data: dict) -> FindingSourceDetail:
    out: FindingSourceDetail = {}  # type: ignore[typeddict-item]
    if "accessPointArn" in data:
        out["access_point_arn"] = data["accessPointArn"]
    if "accessPointAccount" in data:
        out["access_point_account"] = data["accessPointAccount"]
    return out
