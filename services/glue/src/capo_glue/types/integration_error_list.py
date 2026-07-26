"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration_error

IntegrationErrorList: TypeAlias = list[
    "capo_glue.types.integration_error.IntegrationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationErrorList) -> list:
    import capo_glue.types.integration_error

    out: list = []
    for item in value:
        out.append(capo_glue.types.integration_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationErrorList:
    import capo_glue.types.integration_error

    out: IntegrationErrorList = []
    for item in data:
        out.append(capo_glue.types.integration_error.deserialize_aws_json_1_1(item))
    return out
