"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCisTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.target_account_list
    import aws_sdk_inspector2.types.target_resource_tags


class UpdateCisTargets(TypedDict, closed=True):
    account_ids: NotRequired[
        "aws_sdk_inspector2.types.target_account_list.TargetAccountList"
    ]
    """<p>The target account ids.</p>"""
    target_resource_tags: NotRequired[
        "aws_sdk_inspector2.types.target_resource_tags.TargetResourceTags"
    ]
    """<p>The target resource tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCisTargets) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_inspector2.types.target_account_list

        out["accountIds"] = aws_sdk_inspector2.types.target_account_list.serialize_json(
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


def deserialize_json(data: dict) -> UpdateCisTargets:
    out: UpdateCisTargets = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.target_account_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.target_account_list.deserialize_json(
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
