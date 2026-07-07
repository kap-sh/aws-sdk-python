"""Generated from Smithy shape ``com.amazonaws.controlcatalog#Mapping``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.common_control_mapping_details
    import aws_sdk_controlcatalog.types.framework_mapping_details
    import aws_sdk_controlcatalog.types.related_control_mapping_details


class _Mapping_Framework(TypedDict, closed=True):
    Framework: (
        "aws_sdk_controlcatalog.types.framework_mapping_details.FrameworkMappingDetails"
    )


class _Mapping_CommonControl(TypedDict, closed=True):
    CommonControl: "aws_sdk_controlcatalog.types.common_control_mapping_details.CommonControlMappingDetails"


class _Mapping_RelatedControl(TypedDict, closed=True):
    RelatedControl: "aws_sdk_controlcatalog.types.related_control_mapping_details.RelatedControlMappingDetails"


Mapping: TypeAlias = (
    _Mapping_Framework | _Mapping_CommonControl | _Mapping_RelatedControl
)


# --- restJson1 ser/de ---
def serialize_json(value: Mapping) -> dict:
    if "Framework" in value:
        import aws_sdk_controlcatalog.types.framework_mapping_details

        return {
            "Framework": aws_sdk_controlcatalog.types.framework_mapping_details.serialize_json(
                value["Framework"]
            )
        }
    elif "CommonControl" in value:
        import aws_sdk_controlcatalog.types.common_control_mapping_details

        return {
            "CommonControl": aws_sdk_controlcatalog.types.common_control_mapping_details.serialize_json(
                value["CommonControl"]
            )
        }
    elif "RelatedControl" in value:
        import aws_sdk_controlcatalog.types.related_control_mapping_details

        return {
            "RelatedControl": aws_sdk_controlcatalog.types.related_control_mapping_details.serialize_json(
                value["RelatedControl"]
            )
        }
    else:
        raise SerializationError("Mapping: no variant present")


def deserialize_json(data: dict) -> Mapping:
    if "Framework" in data:
        import aws_sdk_controlcatalog.types.framework_mapping_details

        return {
            "Framework": aws_sdk_controlcatalog.types.framework_mapping_details.deserialize_json(
                data["Framework"]
            )
        }
    elif "CommonControl" in data:
        import aws_sdk_controlcatalog.types.common_control_mapping_details

        return {
            "CommonControl": aws_sdk_controlcatalog.types.common_control_mapping_details.deserialize_json(
                data["CommonControl"]
            )
        }
    elif "RelatedControl" in data:
        import aws_sdk_controlcatalog.types.related_control_mapping_details

        return {
            "RelatedControl": aws_sdk_controlcatalog.types.related_control_mapping_details.deserialize_json(
                data["RelatedControl"]
            )
        }
    else:
        raise DeserializationError("Mapping: no recognized variant key")
