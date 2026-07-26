"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration

IntegrationsList: TypeAlias = list["capo_glue.types.integration.Integration"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationsList) -> list:
    import capo_glue.types.integration

    out: list = []
    for item in value:
        out.append(capo_glue.types.integration.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationsList:
    import capo_glue.types.integration

    out: IntegrationsList = []
    for item in data:
        out.append(capo_glue.types.integration.deserialize_aws_json_1_1(item))
    return out
