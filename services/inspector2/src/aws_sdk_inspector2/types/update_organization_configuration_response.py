"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateOrganizationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.auto_enable


class UpdateOrganizationConfigurationResponse(TypedDict, closed=True):
    auto_enable: "aws_sdk_inspector2.types.auto_enable.AutoEnable"
    """<p>The updated status of scan types automatically enabled for new members of your Amazon Inspector organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.auto_enable

    out["autoEnable"] = aws_sdk_inspector2.types.auto_enable.serialize_json(
        value["auto_enable"]
    )
    return out


def deserialize_json(data: dict) -> UpdateOrganizationConfigurationResponse:
    out: UpdateOrganizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        import aws_sdk_inspector2.types.auto_enable

        out["auto_enable"] = aws_sdk_inspector2.types.auto_enable.deserialize_json(
            data["autoEnable"]
        )
    else:
        raise DeserializationError(
            "UpdateOrganizationConfigurationResponse.auto_enable required"
        )
    return out
