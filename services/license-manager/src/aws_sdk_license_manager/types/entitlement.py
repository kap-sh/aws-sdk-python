"""Generated from Smithy shape ``com.amazonaws.licensemanager#Entitlement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_boolean
    import aws_sdk_license_manager.types.entitlement_unit
    import aws_sdk_license_manager.types.long
    import aws_sdk_license_manager.types.string


class Entitlement(TypedDict, closed=True):
    name: "aws_sdk_license_manager.types.string.String"
    """<p>Entitlement name.</p>"""
    value: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Entitlement resource. Use only if the unit is None.</p>"""
    max_count: NotRequired["aws_sdk_license_manager.types.long.Long"]
    """<p>Maximum entitlement count. Use if the unit is not None.</p>"""
    overage: NotRequired["aws_sdk_license_manager.types.box_boolean.BoxBoolean"]
    """<p>Indicates whether overages are allowed.</p>"""
    unit: "aws_sdk_license_manager.types.entitlement_unit.EntitlementUnit"
    """<p>Entitlement unit.</p>"""
    allow_check_in: NotRequired["aws_sdk_license_manager.types.box_boolean.BoxBoolean"]
    """<p>Indicates whether check-ins are allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entitlement) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "max_count" in value:
        out["MaxCount"] = value["max_count"]
    if "overage" in value:
        out["Overage"] = value["overage"]
    import aws_sdk_license_manager.types.entitlement_unit

    out["Unit"] = aws_sdk_license_manager.types.entitlement_unit.serialize_aws_json_1_1(
        value["unit"]
    )
    if "allow_check_in" in value:
        out["AllowCheckIn"] = value["allow_check_in"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Entitlement.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    if "MaxCount" in data:
        out["max_count"] = data["MaxCount"]
    if "Overage" in data:
        out["overage"] = data["Overage"]
    if "Unit" in data:
        import aws_sdk_license_manager.types.entitlement_unit

        out["unit"] = (
            aws_sdk_license_manager.types.entitlement_unit.deserialize_aws_json_1_1(
                data["Unit"]
            )
        )
    else:
        raise DeserializationError("Entitlement.unit required")
    if "AllowCheckIn" in data:
        out["allow_check_in"] = data["AllowCheckIn"]
    return out
