"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCisTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.target_account_list
    import aws_sdk_inspector2.types.target_resource_tags


class CreateCisTargets(TypedDict, closed=True):
    account_ids: "aws_sdk_inspector2.types.target_account_list.TargetAccountList"
    """<p>The CIS target account ids.</p>"""
    target_resource_tags: (
        "aws_sdk_inspector2.types.target_resource_tags.TargetResourceTags"
    )
    """<p>The CIS target resource tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCisTargets) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.target_account_list

    out["accountIds"] = aws_sdk_inspector2.types.target_account_list.serialize_json(
        value["account_ids"]
    )
    import aws_sdk_inspector2.types.target_resource_tags

    out["targetResourceTags"] = (
        aws_sdk_inspector2.types.target_resource_tags.serialize_json(
            value["target_resource_tags"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateCisTargets:
    out: CreateCisTargets = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.target_account_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.target_account_list.deserialize_json(
                data["accountIds"]
            )
        )
    else:
        raise DeserializationError("CreateCisTargets.account_ids required")
    if "targetResourceTags" in data:
        import aws_sdk_inspector2.types.target_resource_tags

        out["target_resource_tags"] = (
            aws_sdk_inspector2.types.target_resource_tags.deserialize_json(
                data["targetResourceTags"]
            )
        )
    else:
        raise DeserializationError("CreateCisTargets.target_resource_tags required")
    return out
