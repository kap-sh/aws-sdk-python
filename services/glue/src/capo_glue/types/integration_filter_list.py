"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration_filter

IntegrationFilterList: TypeAlias = list[
    "capo_glue.types.integration_filter.IntegrationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationFilterList) -> list:
    import capo_glue.types.integration_filter

    out: list = []
    for item in value:
        out.append(capo_glue.types.integration_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationFilterList:
    import capo_glue.types.integration_filter

    out: IntegrationFilterList = []
    for item in data:
        out.append(capo_glue.types.integration_filter.deserialize_aws_json_1_1(item))
    return out
