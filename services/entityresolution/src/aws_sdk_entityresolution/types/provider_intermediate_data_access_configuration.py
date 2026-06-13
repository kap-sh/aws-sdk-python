"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderIntermediateDataAccessConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.aws_account_id_list
    import aws_sdk_entityresolution.types.required_bucket_actions_list


class ProviderIntermediateDataAccessConfiguration(TypedDict):
    aws_account_ids: NotRequired[
        "aws_sdk_entityresolution.types.aws_account_id_list.AwsAccountIdList"
    ]
    """<p>The Amazon Web Services account that provider can use to read or write data into the customer's intermediate S3 bucket.</p>"""
    required_bucket_actions: NotRequired[
        "aws_sdk_entityresolution.types.required_bucket_actions_list.RequiredBucketActionsList"
    ]
    """<p>The S3 bucket actions that the provider requires permission for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderIntermediateDataAccessConfiguration) -> dict:
    out: dict = {}
    if "aws_account_ids" in value:
        import aws_sdk_entityresolution.types.aws_account_id_list

        out["awsAccountIds"] = (
            aws_sdk_entityresolution.types.aws_account_id_list.serialize_json(
                value["aws_account_ids"]
            )
        )
    if "required_bucket_actions" in value:
        import aws_sdk_entityresolution.types.required_bucket_actions_list

        out["requiredBucketActions"] = (
            aws_sdk_entityresolution.types.required_bucket_actions_list.serialize_json(
                value["required_bucket_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProviderIntermediateDataAccessConfiguration:
    out: ProviderIntermediateDataAccessConfiguration = {}  # type: ignore[typeddict-item]
    if "awsAccountIds" in data:
        import aws_sdk_entityresolution.types.aws_account_id_list

        out["aws_account_ids"] = (
            aws_sdk_entityresolution.types.aws_account_id_list.deserialize_json(
                data["awsAccountIds"]
            )
        )
    if "requiredBucketActions" in data:
        import aws_sdk_entityresolution.types.required_bucket_actions_list

        out["required_bucket_actions"] = (
            aws_sdk_entityresolution.types.required_bucket_actions_list.deserialize_json(
                data["requiredBucketActions"]
            )
        )
    return out
