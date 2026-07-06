"""Generated from Smithy shape ``com.amazonaws.controlcatalog#RelatedControlMappingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.control_arn
    import aws_sdk_controlcatalog.types.control_relation_type


class RelatedControlMappingDetails(TypedDict, closed=True):
    control_arn: NotRequired["aws_sdk_controlcatalog.types.control_arn.ControlArn"]
    """<p>The unique identifier of a control.</p>"""
    relation_type: (
        "aws_sdk_controlcatalog.types.control_relation_type.ControlRelationType"
    )
    """<p>Returns an enumerated value that represents the relationship between two or more controls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedControlMappingDetails) -> dict:
    out: dict = {}
    if "control_arn" in value:
        out["ControlArn"] = value["control_arn"]
    import aws_sdk_controlcatalog.types.control_relation_type

    out["RelationType"] = (
        aws_sdk_controlcatalog.types.control_relation_type.serialize_json(
            value["relation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RelatedControlMappingDetails:
    out: RelatedControlMappingDetails = {}  # type: ignore[typeddict-item]
    if "ControlArn" in data:
        out["control_arn"] = data["ControlArn"]
    if "RelationType" in data:
        import aws_sdk_controlcatalog.types.control_relation_type

        out["relation_type"] = (
            aws_sdk_controlcatalog.types.control_relation_type.deserialize_json(
                data["RelationType"]
            )
        )
    else:
        raise DeserializationError(
            "RelatedControlMappingDetails.relation_type required"
        )
    return out
