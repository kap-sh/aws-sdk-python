"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean


class ResourceShareConfiguration(TypedDict, closed=True):
    retain_sharing_on_account_leave_organization: NotRequired[
        "aws_sdk_ram.types.boolean.Boolean"
    ]
    """<p>Specifies whether the consumer account retains access to the resource share after leaving the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareConfiguration) -> dict:
    out: dict = {}
    if "retain_sharing_on_account_leave_organization" in value:
        out["retainSharingOnAccountLeaveOrganization"] = value[
            "retain_sharing_on_account_leave_organization"
        ]
    return out


def deserialize_json(data: dict) -> ResourceShareConfiguration:
    out: ResourceShareConfiguration = {}  # type: ignore[typeddict-item]
    if "retainSharingOnAccountLeaveOrganization" in data:
        out["retain_sharing_on_account_leave_organization"] = data[
            "retainSharingOnAccountLeaveOrganization"
        ]
    return out
