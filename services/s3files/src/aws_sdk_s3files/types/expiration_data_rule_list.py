"""Generated from Smithy shape ``com.amazonaws.s3files#ExpirationDataRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3files.types.expiration_data_rule

ExpirationDataRuleList: TypeAlias = list[
    "aws_sdk_s3files.types.expiration_data_rule.ExpirationDataRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationDataRuleList) -> list:
    import aws_sdk_s3files.types.expiration_data_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_s3files.types.expiration_data_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExpirationDataRuleList:
    import aws_sdk_s3files.types.expiration_data_rule

    out: ExpirationDataRuleList = []
    for item in data:
        out.append(aws_sdk_s3files.types.expiration_data_rule.deserialize_json(item))
    return out
