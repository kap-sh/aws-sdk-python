"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean


class UpdateOrganizationConfigurationRequest(TypedDict):
    auto_enable: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether to enable Amazon Macie automatically for accounts that are added to the organization in Organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    return out


def deserialize_json(data: dict) -> UpdateOrganizationConfigurationRequest:
    out: UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    return out
