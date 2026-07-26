"""Generated from Smithy shape ``com.amazonaws.emr#BootstrapActionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.bootstrap_action_detail

BootstrapActionDetailList: TypeAlias = list[
    "capo_emr.types.bootstrap_action_detail.BootstrapActionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BootstrapActionDetailList) -> list:
    import capo_emr.types.bootstrap_action_detail

    out: list = []
    for item in value:
        out.append(capo_emr.types.bootstrap_action_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BootstrapActionDetailList:
    import capo_emr.types.bootstrap_action_detail

    out: BootstrapActionDetailList = []
    for item in data:
        out.append(
            capo_emr.types.bootstrap_action_detail.deserialize_aws_json_1_1(item)
        )
    return out
