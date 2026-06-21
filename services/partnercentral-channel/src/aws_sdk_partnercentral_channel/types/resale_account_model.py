"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ResaleAccountModel``."""

from typing import Literal, TypeAlias, cast

ResaleAccountModel: TypeAlias = Literal[
    "DISTRIBUTOR",
    "END_CUSTOMER",
    "SOLUTION_PROVIDER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResaleAccountModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResaleAccountModel:
    return cast(ResaleAccountModel, data)
