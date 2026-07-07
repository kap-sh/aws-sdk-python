"""Generated from Smithy shape ``com.amazonaws.auditmanager#ServiceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.aws_service_name
    import aws_sdk_auditmanager.types.non_empty_string


class ServiceMetadata(TypedDict, closed=True):
    name: NotRequired["aws_sdk_auditmanager.types.aws_service_name.AWSServiceName"]
    """<p> The name of the Amazon Web Services service. </p>"""
    display_name: NotRequired[
        "aws_sdk_auditmanager.types.non_empty_string.NonEmptyString"
    ]
    """<p> The display name of the Amazon Web Services service. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of the Amazon Web Services service. </p>"""
    category: NotRequired["aws_sdk_auditmanager.types.non_empty_string.NonEmptyString"]
    """<p> The category that the Amazon Web Services service belongs to, such as compute, storage, or database. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> ServiceMetadata:
    out: ServiceMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "category" in data:
        out["category"] = data["category"]
    return out
