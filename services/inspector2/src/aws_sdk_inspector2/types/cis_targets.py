"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_account_id_list
    import aws_sdk_inspector2.types.target_resource_tags


class CisTargets(TypedDict, closed=True):
    account_ids: NotRequired[
        "aws_sdk_inspector2.types.cis_account_id_list.CisAccountIdList"
    ]
    """<p>The CIS target account ids.</p>"""
    target_resource_tags: NotRequired[
        "aws_sdk_inspector2.types.target_resource_tags.TargetResourceTags"
    ]
    """<p>The CIS target resource tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisTargets) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_inspector2.types.cis_account_id_list

        out["accountIds"] = aws_sdk_inspector2.types.cis_account_id_list.serialize_json(
            value["account_ids"]
        )
    if "target_resource_tags" in value:
        import aws_sdk_inspector2.types.target_resource_tags

        out["targetResourceTags"] = (
            aws_sdk_inspector2.types.target_resource_tags.serialize_json(
                value["target_resource_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisTargets:
    out: CisTargets = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.cis_account_id_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.cis_account_id_list.deserialize_json(
                data["accountIds"]
            )
        )
    if "targetResourceTags" in data:
        import aws_sdk_inspector2.types.target_resource_tags

        out["target_resource_tags"] = (
            aws_sdk_inspector2.types.target_resource_tags.deserialize_json(
                data["targetResourceTags"]
            )
        )
    return out
