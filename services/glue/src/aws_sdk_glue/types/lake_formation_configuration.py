"""Generated from Smithy shape ``com.amazonaws.glue#LakeFormationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.account_id
    import aws_sdk_glue.types.nullable_boolean


class LakeFormationConfiguration(TypedDict, closed=True):
    use_lake_formation_credentials: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to use Lake Formation credentials for the crawler instead of the IAM role credentials.</p>"""
    account_id: NotRequired["aws_sdk_glue.types.account_id.AccountId"]
    """<p>Required for cross account crawls. For same account crawls as the target data, this can be left as null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LakeFormationConfiguration) -> dict:
    out: dict = {}
    if "use_lake_formation_credentials" in value:
        out["UseLakeFormationCredentials"] = value["use_lake_formation_credentials"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LakeFormationConfiguration:
    out: LakeFormationConfiguration = {}  # type: ignore[typeddict-item]
    if "UseLakeFormationCredentials" in data:
        out["use_lake_formation_credentials"] = data["UseLakeFormationCredentials"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
