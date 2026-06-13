"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.control_arn
    import aws_sdk_controlcatalog.types.mapping
    import aws_sdk_controlcatalog.types.mapping_type


class ControlMapping(TypedDict):
    control_arn: "aws_sdk_controlcatalog.types.control_arn.ControlArn"
    """<p>The Amazon Resource Name (ARN) that identifies the control in the mapping.</p>"""
    mapping_type: "aws_sdk_controlcatalog.types.mapping_type.MappingType"
    """<p>The type of mapping relationship between the control and other entities.</p>"""
    mapping: "aws_sdk_controlcatalog.types.mapping.Mapping"
    """<p>The details of the mapping relationship, for example, containing framework, common control, or related control information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlMapping) -> dict:
    out: dict = {}
    out["ControlArn"] = value["control_arn"]
    import aws_sdk_controlcatalog.types.mapping_type

    out["MappingType"] = aws_sdk_controlcatalog.types.mapping_type.serialize_json(
        value["mapping_type"]
    )
    import aws_sdk_controlcatalog.types.mapping

    out["Mapping"] = aws_sdk_controlcatalog.types.mapping.serialize_json(
        value["mapping"]
    )
    return out


def deserialize_json(data: dict) -> ControlMapping:
    out: ControlMapping = {}  # type: ignore[typeddict-item]
    if "ControlArn" in data:
        out["control_arn"] = data["ControlArn"]
    else:
        raise DeserializationError("ControlMapping.control_arn required")
    if "MappingType" in data:
        import aws_sdk_controlcatalog.types.mapping_type

        out["mapping_type"] = (
            aws_sdk_controlcatalog.types.mapping_type.deserialize_json(
                data["MappingType"]
            )
        )
    else:
        raise DeserializationError("ControlMapping.mapping_type required")
    if "Mapping" in data:
        import aws_sdk_controlcatalog.types.mapping

        out["mapping"] = aws_sdk_controlcatalog.types.mapping.deserialize_json(
            data["Mapping"]
        )
    else:
        raise DeserializationError("ControlMapping.mapping required")
    return out
