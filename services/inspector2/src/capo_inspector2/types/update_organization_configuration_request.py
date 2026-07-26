"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.auto_enable


class UpdateOrganizationConfigurationRequest(TypedDict, closed=True):
    auto_enable: "capo_inspector2.types.auto_enable.AutoEnable"
    """<p>Defines which scan types are enabled automatically for new members of your Amazon Inspector organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    import capo_inspector2.types.auto_enable

    out["autoEnable"] = capo_inspector2.types.auto_enable.serialize_json(
        value["auto_enable"]
    )
    return out


def deserialize_json(data: dict) -> UpdateOrganizationConfigurationRequest:
    out: UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        import capo_inspector2.types.auto_enable

        out["auto_enable"] = capo_inspector2.types.auto_enable.deserialize_json(
            data["autoEnable"]
        )
    else:
        raise DeserializationError(
            "UpdateOrganizationConfigurationRequest.auto_enable required"
        )
    return out
