"""Generated from Smithy shape ``com.amazonaws.connect#DataTableAccessControlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.primary_attribute_access_control_configuration_item


class DataTableAccessControlConfiguration(TypedDict, closed=True):
    primary_attribute_access_control_configuration: NotRequired[
        "capo_connect.types.primary_attribute_access_control_configuration_item.PrimaryAttributeAccessControlConfigurationItem"
    ]
    """<p>The configuration's primary attribute access control configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableAccessControlConfiguration) -> dict:
    out: dict = {}
    if "primary_attribute_access_control_configuration" in value:
        import capo_connect.types.primary_attribute_access_control_configuration_item

        out["PrimaryAttributeAccessControlConfiguration"] = (
            capo_connect.types.primary_attribute_access_control_configuration_item.serialize_json(
                value["primary_attribute_access_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataTableAccessControlConfiguration:
    out: DataTableAccessControlConfiguration = {}  # type: ignore[typeddict-item]
    if "PrimaryAttributeAccessControlConfiguration" in data:
        import capo_connect.types.primary_attribute_access_control_configuration_item

        out["primary_attribute_access_control_configuration"] = (
            capo_connect.types.primary_attribute_access_control_configuration_item.deserialize_json(
                data["PrimaryAttributeAccessControlConfiguration"]
            )
        )
    return out
