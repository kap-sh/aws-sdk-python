"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ConstraintSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.constraint_description
    import aws_sdk_service_catalog.types.constraint_type


class ConstraintSummary(TypedDict):
    type: NotRequired["aws_sdk_service_catalog.types.constraint_type.ConstraintType"]
    """<p>The type of constraint.</p> <ul> <li> <p> <code>LAUNCH</code> </p> </li> <li> <p> <code>NOTIFICATION</code> </p> </li> <li> <p>STACKSET</p> </li> <li> <p> <code>TEMPLATE</code> </p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.constraint_description.ConstraintDescription"
    ]
    """<p>The description of the constraint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintSummary) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConstraintSummary:
    out: ConstraintSummary = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
