"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCrossAccountResourceAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.aws_account_ids


class ListCrossAccountResourceAccountsResponse(TypedDict, closed=True):
    resource_owner_aws_account_ids: NotRequired[
        "aws_sdk_global_accelerator.types.aws_account_ids.AwsAccountIds"
    ]
    """<p>The account IDs of principals (resource owners) in a cross-account attachment who can work with resources listed in the same attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCrossAccountResourceAccountsResponse) -> dict:
    out: dict = {}
    if "resource_owner_aws_account_ids" in value:
        import aws_sdk_global_accelerator.types.aws_account_ids

        out["ResourceOwnerAwsAccountIds"] = (
            aws_sdk_global_accelerator.types.aws_account_ids.serialize_aws_json_1_1(
                value["resource_owner_aws_account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCrossAccountResourceAccountsResponse:
    out: ListCrossAccountResourceAccountsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceOwnerAwsAccountIds" in data:
        import aws_sdk_global_accelerator.types.aws_account_ids

        out["resource_owner_aws_account_ids"] = (
            aws_sdk_global_accelerator.types.aws_account_ids.deserialize_aws_json_1_1(
                data["ResourceOwnerAwsAccountIds"]
            )
        )
    return out
