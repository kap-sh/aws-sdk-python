"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentResolvedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_id
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region


class EnvironmentResolvedAccount(TypedDict, closed=True):
    aws_account_id: "aws_sdk_datazone.types.aws_account_id.AwsAccountId"
    """<p>The ID of the resolved account.</p>"""
    region_name: "aws_sdk_datazone.types.aws_region.AwsRegion"
    """<p>The name of the resolved Region.</p>"""
    source_account_pool_id: NotRequired[
        "aws_sdk_datazone.types.account_pool_id.AccountPoolId"
    ]
    """<p>The ID of the account pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentResolvedAccount) -> dict:
    out: dict = {}
    out["awsAccountId"] = value["aws_account_id"]
    out["regionName"] = value["region_name"]
    if "source_account_pool_id" in value:
        out["sourceAccountPoolId"] = value["source_account_pool_id"]
    return out


def deserialize_json(data: dict) -> EnvironmentResolvedAccount:
    out: EnvironmentResolvedAccount = {}  # type: ignore[typeddict-item]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        raise DeserializationError("EnvironmentResolvedAccount.aws_account_id required")
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    else:
        raise DeserializationError("EnvironmentResolvedAccount.region_name required")
    if "sourceAccountPoolId" in data:
        out["source_account_pool_id"] = data["sourceAccountPoolId"]
    return out
