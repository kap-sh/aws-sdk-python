"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LaunchTemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_id
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.launch_template_id


class LaunchTemplateConfiguration(TypedDict, closed=True):
    launch_template_id: "capo_imagebuilder.types.launch_template_id.LaunchTemplateId"
    """<p>Identifies the Amazon EC2 launch template to use.</p>"""
    account_id: NotRequired["capo_imagebuilder.types.account_id.AccountId"]
    """<p>The account ID that this configuration applies to.</p>"""
    set_default_version: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Set the specified Amazon EC2 launch template as the default launch template for the specified account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateConfiguration) -> dict:
    out: dict = {}
    out["launchTemplateId"] = value["launch_template_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    out["setDefaultVersion"] = value.get("set_default_version", False)
    return out


def deserialize_json(data: dict) -> LaunchTemplateConfiguration:
    out: LaunchTemplateConfiguration = {}  # type: ignore[typeddict-item]
    if "launchTemplateId" in data:
        out["launch_template_id"] = data["launchTemplateId"]
    else:
        raise DeserializationError(
            "LaunchTemplateConfiguration.launch_template_id required"
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "setDefaultVersion" in data:
        out["set_default_version"] = data["setDefaultVersion"]
    else:
        out["set_default_version"] = False
    return out
