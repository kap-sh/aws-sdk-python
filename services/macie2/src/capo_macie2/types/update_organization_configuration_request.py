"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean


class UpdateOrganizationConfigurationRequest(TypedDict, closed=True):
    auto_enable: NotRequired["capo_macie2.types.__boolean.__boolean"]
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
