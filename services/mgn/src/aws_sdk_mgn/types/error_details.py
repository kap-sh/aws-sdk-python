"""Generated from Smithy shape ``com.amazonaws.mgn#ErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.large_bounded_string


class ErrorDetails(TypedDict):
    message: NotRequired["aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Error details message.</p>"""
    code: NotRequired["aws_sdk_mgn.types.bounded_string.BoundedString"]
    """<p>Error details code.</p>"""
    resource_id: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Error details resourceId.</p>"""
    resource_type: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Error details resourceType.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out
