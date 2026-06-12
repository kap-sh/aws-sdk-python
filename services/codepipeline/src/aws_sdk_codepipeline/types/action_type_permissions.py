"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypePermissions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.allowed_accounts


class ActionTypePermissions(TypedDict):
    allowed_accounts: "aws_sdk_codepipeline.types.allowed_accounts.AllowedAccounts"
    """<p>A list of Amazon Web Services account IDs with access to use the action type in their pipelines.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypePermissions) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.allowed_accounts

    out["allowedAccounts"] = (
        aws_sdk_codepipeline.types.allowed_accounts.serialize_aws_json_1_1(
            value["allowed_accounts"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypePermissions:
    out: ActionTypePermissions = {}  # type: ignore[typeddict-item]
    if "allowedAccounts" in data:
        import aws_sdk_codepipeline.types.allowed_accounts

        out["allowed_accounts"] = (
            aws_sdk_codepipeline.types.allowed_accounts.deserialize_aws_json_1_1(
                data["allowedAccounts"]
            )
        )
    else:
        raise DeserializationError("ActionTypePermissions.allowed_accounts required")
    return out
