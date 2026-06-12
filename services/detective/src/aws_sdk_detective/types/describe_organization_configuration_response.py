"""Generated from Smithy shape ``com.amazonaws.detective#DescribeOrganizationConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.boolean


class DescribeOrganizationConfigurationResponse(TypedDict):
    auto_enable: "aws_sdk_detective.types.boolean.Boolean"
    """<p>Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationConfigurationResponse) -> dict:
    out: dict = {}
    out["AutoEnable"] = value.get("auto_enable", False)
    return out


def deserialize_json(data: dict) -> DescribeOrganizationConfigurationResponse:
    out: DescribeOrganizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AutoEnable" in data:
        out["auto_enable"] = data["AutoEnable"]
    else:
        out["auto_enable"] = False
    return out
